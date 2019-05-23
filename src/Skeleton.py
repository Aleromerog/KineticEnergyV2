from src.ReadFile import ReadFile
import datetime


class Skeleton:
    def __init__ (self, file_name):
        self.file = file_name
        self.kinetic_energy = 0.0
           
    def get_skeleton_joints(self):
        return ReadFile.read(self.file)
    
    def geet_time(self, time, previous_time):
        date_time_str = previous_time
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        date_time_str2 = time
        date_time_obj2 = datetime.datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S.%f')
        minu = date_time_obj2 - date_time_obj
        return(minu.microseconds/1e6)
                
    def get_mass(self):
        # JOINTS POSITIONS:
            # 0.  VLElbow
            # 1.  VRElbow
            # 2.  VLFoot
            # 3.  VRFoot
            # 4.  VLHand
            # 5.  VRHand
            # 6.  VHead
            # 7.  VLHip
            # 8.  VRHip
            # 9.  VLKnee
            # 10. VRKnee
            # 11. VLShoulder
            # 12. VRShoulder
            # 13. VTorsoBase
            # 14. VTorsoMid
            # 15. VTorsoUpper

        mass = [0.7139953, #0
                0.7139953, #1
                0.512359,  #2
                0.512359,  #3
                0.272855,  #4
                0.272855,  #5
                3.987231,  #6
                4.964321,  #7
                4.964321,  #8
                1.535642,  #9
                1.535642,  #10
                1.028092,  #11
                1.028092,  #12
                6.456848,  #13
                6.335836,  #14
                7.060998]  #15
        return mass  

    def get_kinetic_energy(self):
        skeletons = self.get_skeleton_joints()
        self.kinetic_energy = 0.0
        mass = self.get_mass()
        for num in range(len(skeletons)-1):
            for joint in range(1, 17):
                time = self.geet_time(skeletons[num+1][0], skeletons[num][0])
                if time != 0 or time != None: 
                    xi = (float(skeletons[num+1][joint*3-2]) - float(skeletons[num][joint*3-2]))
                    yi = (float(skeletons[num+1][joint*3-1]) - float(skeletons[num][joint*3-1]))
                    zi = (float(skeletons[num+1][joint*3]) - float(skeletons[num][joint*3]))
                    distance = ((xi**2) + (yi**2) + (zi**2))**(1/2)
                    velocity = distance / time
                    self.kinetic_energy += (mass[joint-1] * velocity**2)/2
                
                else:
                    continue
        return self.kinetic_energy

    def get_calories(self):
        # Referene caloric energy: https://www.zonadiet.com/nutricion/energia.htm
        if self.kinetic_energy != 0.0:
            return (self.kinetic_energy * 1e3)/4184
        else:
            self.get_kinetic_energy()
            return (self.kinetic_energy * 1e3)/4184
