# -*- coding: utf-8 -*-

import arcpy


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]


class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Graduated Color Renderer"
        self.description = "create a graduated color map based a specific attribute of a layer."
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        #parameter definitions

        # Parameter 0: Input ArcGIS Pro Project Name
        param0 = arcpy.parameter(
            displayName = "Input ArcGIS Pro Project Name",
            name = "aprxInputName",
            datatype = "DEFile",
            parameterType = "Required",
            direction = "Input"
        )
        # Parameter 1: which layer you want to classify to create a color map
        param1 = arcpy.Parameter(
            displayName = "Layer to Classify",
            name = "LayertoClassify",
            datatype = "GPLayer",
            parameterType = "Required",
            direction = "Input"
        )
        # Parameter 2: Output Folder Location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        # Parameter 3: Output Project Name
        param3 = arcpy.Parameter(
            displayName ="Output Project Name",
            name = "OutputProjectName",
            datatype ="GPString",
            parameterType ="Required",
            direction ="Input"
        )
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # Define Progressor Variables
        readTime = 3    #the time for users to read the progress
        start = 0       #beginning position of the progressor
        max = 100       #end position of the progressor
        step = 33       #the progress interval to move the progressor forward

        # Setup Progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) #pause for users to read the progress message

        #add message to the results pane
        arcpy.AddMessage("Validating Project File...")

        #Project file
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)

        #Grabs the first instance of a map from the .aprx file
        campus = project.listMaps('Map')[0]

        #Increment Progressor
        arcpy.SetProgressorPosition(start + step) #now is 33% complete
        arcpy.SetProgressorLabel("Finding your map layer...") #update the progress message
        time.sleep(readTime) #pause for users to read the progress message

        #Loop through the layers in the map
        for layer in campus.listLayers():
            if layer.isFeatureLayer: #if the layer is a feature layer
                symbology = layer.symbology #copy the symbology of the layer
                if hasattr(symbology, 'renderer'): # make sure the symbology has renderer attributes
                    if layer.name == parameters[1].valueAsText: #check if the layer name matches the input layer

                        #Increment Progressor
                        arcpy.SetProgressorPosition(start + step*2) #now is 66% completed
                        arcpy.SetProgressorLabel("Calculating and classifying layer...") #update the progress message
                        time.sleep(readTime) #pause for users to read the progress message
                        arcpy.AddMessage("Calculating and classifying layer...")

                        #Update the Copy's Renderer to "Graduated Colors Renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        #Tell arcpy which field we want to base our chloropleth off of
                        symbology.renderer.classificationField = "Shape_Area"

                        #Set how many classes we'll have for the map
                        symbology.renderer.breakCount = 5

                        #Set Color Ramp
                        symbology.renderer.colorRamp = project.listColorRamps("Oranges (5 Classes)")[0]

                        #Set the Layer's Actual Symbology Equal to the copy's
                        layer.symbology = symbology

                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print ("No layers found.")
        #Increment Progressor to 99% at the end of the tool
        arcpy.SetProgressorPosition(max - 1) #now is 99% completed
        arcpy.SetProgressorLabel("Saving...") #update the progress message 
        time.sleep(readTime) #pause for users to read the progress message
        arcpy.AddMessage("Saving...")

        #Save the project to the output location with the output name
        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx") 
        #parm2 is the output location and parm3 is the output project name              
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
