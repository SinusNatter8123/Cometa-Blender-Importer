import bpy
import re
from math import radians

class CometaBlenderImporter:
    def __init__(self, filepath:str, name_mapping:dict, to_axis:dict):
        got_labels = False
        data = []
        with open(filepath) as f:
            for line in f.readlines()[4:]:
                line = re.split("\t|\n", line)
                line = list(map(lambda x: x.replace("(Deg)", ""), line))
                line = list(map(lambda x: x.replace(" ", ""), line))
                if len(line[0]) == 0:
                    continue
                else:
                    if not got_labels:
                        labels = line
                        got_labels = True
                        continue

                    data.append(line)
        my_data = {}
        for i, label in enumerate(labels[:-1]):
            label = tuple("".join(label).split(":"))
            my_data[label] = []
            for dataline in data[1:]:
                my_data[label].append(float(dataline[i]))
        ordered_data = {}
        time = (k := next(iter(my_data)), my_data.pop(k))
        for k in my_data.keys():
            key = k[0]
            if key not in ordered_data:
                ordered_data[key] = {k[1]: my_data[k]}
            else:
                ordered_data[key][k[1]] = my_data[k]
        self.data = ordered_data
        self.name_mapping = name_mapping
        self.to_axis = to_axis


    def apply_to_armature(self, armature_name:str):
        #clear all other animation data
        obj = bpy.data.objects[armature_name]
        if obj.animation_data:
            obj.animation_data_clear()

        #apply data
        data = self.data
        name_mapping = self.name_mapping
        to_axis = self.to_axis
        for joint_name, all_angles in data.items():
            bone_name = name_mapping.get(joint_name)

            if bone_name:
                bone = bpy.data.objects[armature_name].pose.bones.get(bone_name)
                keys = list(all_angles.keys())

                if bone:
                    print(f"Applying data to bone: {bone_name}")  # Debugging
                    for frame in range(0, len(all_angles[keys[0]]), 10):
                        # Ensure the bone's rotation mode is set correctly
                        bone.rotation_mode = 'XYZ'  # Change to match your data format (e.g., 'XYZ', 'XZY', etc.)
                        sort_lookup = {
                            "X": 0,
                            "Y": 1,
                            "Z": 2
                        }
                        keys.sort(key=lambda x: sort_lookup[to_axis[joint_name][x][0]])
                        bone.rotation_euler = [
                            radians(to_axis[joint_name][keys[0]][1] * all_angles[keys[0]][frame]),
                            radians(to_axis[joint_name][keys[1]][1] * all_angles[keys[1]][frame]),
                            radians(to_axis[joint_name][keys[2]][1] * all_angles[keys[2]][frame])
                        ]

                        # Insert keyframe
                        bone.keyframe_insert(data_path="rotation_euler", frame=frame // 10)
                else:
                    print(f"Bone '{bone_name}' not found in the armature.")  # Debugging
