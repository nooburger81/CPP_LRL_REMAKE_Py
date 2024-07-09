import unreal

#Declare used tool libraries and subsystems
LevelTools = unreal.Level
EditorLevelLibrary = unreal.EditorLevelLibrary
LevelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#Initialize new level variable
NewLevel = "MyNewLevel"

#Create new level
MyNewLevel = LevelSubsys.new_level("/Game/Maps/NewLevel")

#Set level as current level (Open new level)
LevelSubsys.set_current_level_by_name(MyNewLevel)

#Save the new level
LevelSubsys.save_current_level()

