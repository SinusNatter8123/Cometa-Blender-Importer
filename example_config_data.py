name_mapping = {
    "RightElbow": "mixamorig:RightForeArm",
    "Neck": "mixamorig:Neck",
    "RightWrist": "mixamorig:RightHand",
    "LeftWrist": "mixamorig:LeftHand",
    "LeftElbow": "mixamorig:LeftForeArm",
    "RightShoulder": "mixamorig:RightArm",
    "LeftShoulder": "mixamorig:LeftArm"
}


to_axis={
    "RightWrist":{
        "Flexion/Extension":("X",-1),
        "Ulnar/RadialDeviation":("Z",1),
        "CW/CCWRotation":("Y",1)
    },
    "RightElbow":{
        "Flexion/Extension":("Z",-1),
        "Pronation/Supination":("Y",-1),
        "Deviation":("X",-1)
    },
    "RightShoulder":{
        "HorizontalFlexion/Extension":("Z",-1),
        "VerticalFlexion/Extension":("Y",-1),
        "Abduction/Adduction":("X",-1)
    },
    "LeftWrist":{
        "Flexion/Extension":("X",1),
        "Ulnar/RadialDeviation":("Z",1),
        "CW/CCWRotation":("Y",1)
    },
    "LeftElbow":{
        "Flexion/Extension":("Z",1),
        "Pronation/Supination":("Y",-1),
        "Deviation":("X",-1)
    },
    "LeftShoulder":{
        "HorizontalFlexion/Extension":("Z",1),
        "VerticalFlexion/Extension":("Y",-1),
        "Abduction/Adduction":("X",-1)
    },
    "Neck":{
        "Flexion/Extension":("X",-1),
        "CW/CCWRotation":("Y",1),
        "LateralBending":("Z",-1)
    }
}
