import unreal

#This script adds all atmospheric related actors to a scene/level

#Declare variables and subsystems
ActorLocation = unreal.Vector(0, 0, 0)
ActorRotation = unreal.Rotator(0, 0, 0)
Spawnable = unreal.EditorLevelLibrary
LevelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#Create new atmosphere

DirLight = Spawnable.spawn_actor_from_class(unreal.DirectionalLight, ActorLocation)
SkyLight = Spawnable.spawn_actor_from_class(unreal.SkyLight, ActorLocation)
Sky = Spawnable.spawn_actor_from_class(unreal.SkyAtmosphere, ActorLocation)
Fog = Spawnable.spawn_actor_from_class(unreal.ExponentialHeightFog, ActorLocation)
Clouds = Spawnable.spawn_actor_from_class(unreal.VolumetricCloud, ActorLocation)

#Adjust Rotation
#DirLight.set_actor_rotation(ActorRotation)

#Save actors
LevelSubsys.save_current_level()