# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 09:47:26 2020
Module to read out swimming pool enveloping surface data from excel files.
Last modified 2020-09-25 for Project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'
"""
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import teaser.data.input.material_input_json as mat_input
import xlrd
import sys



def load_type_element(element, year, construction, data_class, filePath, sheetNameElements):
    """Load BuildingElement from Excel.

    Loads typical building elements according to their construction year and
    their construction type from an Excel File. 

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    year : int
        Year of construction

    construction : str
        Construction type, code list ('heavy', 'light', tabula, ...)

    data_class : DataClass()
       DataClass containing the bindings for TypeBuildingElement and
       Material (typically this is the data class stored in prj.data,
                 but the user can individually change that.
                 
    filePath: str
        Path to Excel File.
        
    sheetNameElements: str
        Name of the sheet within the Excel File that contains the element data.
                 
    """

    #Loading the excel sheet
    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetNameElements);
    
    #Parameter to specify success of searching procedure. 
    found=False
    
    col1=getCol("building age", filePath, sheetNameElements)
    col2=col1+1
    startRow=getRow("OuterWall", filePath, sheetNameElements)
    
    for i in range(startRow, sheet.nrows):
        ageMin=sheet.cell_value(i, col1)
        ageMax=sheet.cell_value(i, col2)
        #Comparison of building age and element type with table entries to identify suitable data.
        if (
            ageMin != ""
            and ageMin <= float(year) <= ageMax
            and sheet.cell_value(i,0).startswith(type(element).__name__)
        ):
            found=True            
            
            # print("Wähle Bauteil", type(element).__name__)
            #Saving element data in respective element class
            _set_basic_data(element, inSheet=sheet, inRow=i)
            
            #Counting material layers           
            numLayers=1   
            while (i+numLayers < sheet.nrows and sheet.cell_value(i + numLayers, 0)==""):
                numLayers+=1
            
            #Loading material data. Material will be ignored if ID is missing. 
            #Thickness will be set to 0.01 m if data is missing in Excel table.
            colMaterialId=getCol("material id", filePath, sheetNameElements)
            #In actual version of table there are two thicknesses given. Reading from [cm].
            colThickness=getCol("thickness", filePath, sheetNameElements)+1
            for k in range(numLayers):
                if sheet.cell_value(i + k, colMaterialId) != "":
                    layer = Layer(element)
                    layer.id = k
                    
                    if sheet.cell_value(i + k, colThickness) == "" :
                        # print("Missing thickness for layer", k, "of", sheet.cell_value(i, 0))
                        # print("Thickness set to 0.01")
                        # print()
                        layer.thickness = 0.01
                    else:
                        layer.thickness = sheet.cell_value(i + k, colThickness)/100
                    
                    material = Material(layer)
                    mat_input.load_material_id(material, sheet.cell_value(i + k, colMaterialId), data_class)
                    #print("For Element", type(element).__name__, "chosen structure", sheet.cell_value(i,0),
                          #"layer", layer.id, "thickness", layer.thickness)
    
    #The application will be aborted if no element data was found. 
    #This would lead to calculation errors and a crash of the application.
    if not (found):
        print("Error: No element data found for", type(element).__name__)
        print("Please check the Excel File, maybe the bulding age is missing",
              "or the keyword in method getKeyword is wrong")
        sys.exit("Program aborted")



                    
   

def _set_basic_data(element, inSheet, inRow):
    """Set basic data for building elements.

    Helper function to set basic data.

    Parameters
    ----------
    element : BuildingElement
        BuildingElement
    inSheet :
        Excel file with element data
    inRow :
        Row number of the respective element in the Excel file

    """
    
    #Setting radiation and convection according to json-database from teaser.    
    element.building_age_group = [inSheet.cell_value(inRow, 1), inSheet.cell_value(inRow, 2)]
    element.construction_type = "heavy"
    element.inner_radiation = 5.0
    element.inner_convection = 2.7

    #According to the Teaser-database, the element types OuterWall and Door 
    #share the same radiation and convection.
    #Same for GroundFoor, Floor and Ceiling.
    if (
        type(element).__name__ == "OuterWall"
        or type(element).__name__ == "Door"
    ):

        element.inner_radiation = 5.0
        element.inner_convection = 2.7
        element.outer_radiation = 5.0
        element.outer_convection = 20.0
        
    elif (type(element).__name__ == "Rooftop"):
        element.inner_radiation = 5.0
        element.inner_convection = 1.7000000000000002
        element.outer_radiation = 5.0
        element.outer_convection = 20.000000000000004
    
    #Calculation for pool areas varies in method calc_ua_value of class buildingelement
    elif (type(element).__name__ == "GroundFloor"
          or type(element).__name__ == "Floor"
          or type(element).__name__ == "Ceiling"):
        element.inner_radiation = 5.0
        element.inner_convection = 1.7000000000000002

  
    #To be changed if different window data should be used. 
    #Replacing element_in[] with inSheet.cell_value(inRow, COLUMN OF WINDOWS)
    
    # elif type(element).__name__ == "Window":

    #     element.outer_radiation = element_in["outer_radiation"]
    #     element.outer_convection = element_in["outer_convection"]
    #     element.g_value = element_in["g_value"]
    #     element.a_conv = element_in["a_conv"]
    #     element.shading_g_total = element_in["shading_g_total"]
    #     element.shading_max_irr = element_in["shading_max_irr"]
                




def getArea(zoneId, element, orientation, filePath, sheetNameAreas, numZones):
    """Loads the building element areas from an Excel file.


    Parameters
    ----------
    zoneID : int
        Auxilary parameter to indicate the respective zone
    
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER


    orientation : int
        Orintation for windows and outer walls

              
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
        
    numZones : int
        Auxilary parameter to indicate the given standard zones (without pool zones)
                 
    """    
    
    #Aufruf der Excel-Datei
    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetNameAreas);
    #Die zu betrachtende Spalte der Excel-Datei wird ausgewählt
    startCol=getCol("Zone 1", filePath, sheetNameAreas) 
    # Gets Data from the Pool
    data = getPoolDataInDict(zoneId, filePath, sheetNameAreas)

    
    #print(zoneId,numZones, type(element).__name__, element.name)
    
    #Keywords to find the respective element in the Excel table. If changes to
    #the table are applied, please make sure to adjust the keywords.
    if (zoneId<8 and element.name=="GroundFloor"): 
        row1 = getRow("Total area of zone", filePath, sheetNameAreas)
        row2 = getRow("Traffic and common area", filePath, sheetNameAreas) 
        col = startCol + 2*zoneId + 1        

        if (sheet.cell_value(row1, col)==""):
            value1=0
        else:
            value1 = sheet.cell_value(row1, col)    
                
        if (sheet.cell_value(row2, col)==""):
            value2=0
        else:
            value2 = sheet.cell_value(row2, col)    
                
        if (element.parent.name.startswith("Schwimmhalle")):
            data = getPoolDataInDict("SUM", filePath, sheetNameAreas)
            value3 = data['Water surface']

            if (value1-value2-value3==0):
                return float(0.001)
            else:
                return value1-value2-value3 
        
        else:             
            if (value1-value2==0):
                return float(0.001)
            else:
                return value1-value2      
        
    elif (zoneId>=8 and element.name=="PoolFloorWithEarthContact"):
        area = data['Pool floor with earth contact']
        if (element.name=="PoolFloorWithEarthContact"):
            if (area == "" or area == 0):
                return float(0.001)
            else:
                return area
    
    #OuterWalls for pools based on 'Koordinierungskreis Bäder (KOK) -
    #Richtlinien für den Bäderbau 2013'
    elif (zoneId>=8 and type(element).__name__=="Window"):    
        return float(0.001)
    
    elif (zoneId>=8 and type(element).__name__=="OuterWall"):
        area1 = data['Water surface']
        area2 = data['Water volume']
        height = area2 / area1
        if area1 < 125:
            # Square area
            length = area1 ** (1/2)
        elif (area1 >= 125 or area1 <= 312.5):
            length = 25    
        else:
            length = 50
            
        width = area1 / length 
        if element.orientation == 0 or element.orientation == 180:
            return (width*height)
        else:
            return (length*height)
            
    else:  
        keyword = getKeyword(type(element).__name__, filePath, sheetNameAreas)
        row=getRow(keyword, filePath, sheetNameAreas)
        col=startCol + 2*zoneId +1

        if ((type(element).__name__=="OuterWall" 
             or type(element).__name__ == "Window") 
            and element.orientation>0):
            row += int(element.orientation/90)

        if (sheet.cell_value(row, col)=="" or sheet.cell_value(row, col)==0.0):
            return float(0.001)
        else:
            return float(sheet.cell_value(row, col))  
 
    print("Area of element", type(element).__name__, "not found.")
    return float(0.001)
        




def getInnerArea(zoneId, element, filePath, sheetNameAreas, zoneAreas, numZones):
    """Loads the inner building element areas from an Excel file.


    Parameters
    ----------
    zoneID : int
        Auxilary parameter to indicate the respective zone
    
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER


    orientation : int
        Orintation for windows and outer walls

              
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
        
    numZones : int
        Auxilary parameter to indicate the given standard zones (without pool zones)
                 
    """        
    
    #Aufruf der Excel-Datei
    wb = xlrd.open_workbook(filePath)
    sheet = wb.sheet_by_name(sheetNameAreas)
    startCol = getCol("Zone 1", filePath, sheetNameAreas)
    # Gets Data from the Pools
    data = getPoolDataInDict(zoneId, filePath, sheetNameAreas)


    if(element.parent.name == "Technikraum"):
     
        if(element.name.startswith("CeilingUnderPoolArea")):
            zoneId = (int(element.name[-1]) + 7)
            data = getPoolDataInDict(zoneId, filePath, sheetNameAreas)
            area1 = data['Water surface']
            area2 = data['Pool floor with earth contact']
            if (area2 ==""):
                area2 = 0.0
            return (area1 - area2)
                
                
        elif(element.name.startswith("CeilingUnderTrafficAndCommonAreas")):
            row = getRow("Traffic and common", filePath, sheetNameAreas)
            col = getCol("Zone 4", filePath, sheetNameAreas)+1
            if (sheet.cell_value(row, col)=="" or sheet.cell_value(row, col)==0.0):
                return float(0.0)
            else:
                return sheet.cell_value(row, col)
    
    #Keywords to find the respective element in the Excel table. If changes to
    #the table are applied, please make sure to adjust the keywords.
    #Consider that the methods getCol and getRow only work without line breaks
    elif (element.name.startswith("PoolAreaAboveTechnicalRoom")):
        area1 = data['Water surface']
        area2 = data['Pool floor with earth contact']
        
        if (area1 - area2 == 0):
            return float(0.001)
        else:
            return (area1 - area2)
        
    elif (element.name.startswith("TrafficAndCommonAreasAboveTechnicalRoom")):
        row = getRow("Traffic and common", filePath, sheetNameAreas) 
        col = startCol + 2*zoneId + 1
        if (sheet.cell_value(row, col) == 0):
            return float(0.001)
        else:
            return sheet.cell_value(row, col) 
        
    elif (element.name.startswith("UpperZoneLimitationOfPool")
          or element.name.startswith("ContactAreaToWaterSurface")):
        
        if data != 0:
            area = data['Water surface']
        
        if element.parent.name.startswith("Schwimmhalle"):
            ZoneId = (int(element.name[-1]) +7)
            data = getPoolDataInDict(ZoneId, filePath, sheetNameAreas)
            area = data['Water surface']
            
            #row = getRow("Water areas", filePath, sheetNameAreas)
            #row+= int(element.name[-1])-1
        
        if (area == 0):
            return float(0.001)
        else:
            return area

    

   

def getZoneArea(filePath, sheetNameAreas):
    """Loads the zone areas from an Excel file.


    Parameters
    ----------              
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """        

    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetNameAreas);
    numZones = countZones(filePath, sheetNameAreas)
    listZoneAreas=[]    
    startCol=getCol("Zone 1", filePath, sheetNameAreas)    
    row=getRow("Total area of zone", filePath, sheetNameAreas)
    
    for col in range(startCol, 2*numZones, 2):            
        if(sheet.cell_value(row, col+1)==""):
            listZoneAreas.append(0)
        else:
            listZoneAreas.append(sheet.cell_value(row, col+1))
            
    return listZoneAreas





#Searches for the column that starts with the keyword. Only works without line breaks.    
def getCol(keyword, filePath, sheetName):
    """Loads the respective column from the Excel file for
    the given keyword.


    Parameters
    ----------              
    keyword: str
        Keyword to search Excel file
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """   
    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetName);
    for i in range(0, 3):
        for k in range(0, sheet.ncols):
            if sheet.cell_value(i, k).startswith(keyword):
                return k
                
    print("WARNING: Column starting with keyword", keyword, "not found!")
    return 0
       



         
#Searches for the row that starts with the keyword. Only works without line breaks.                 
def getRow(keyword, filePath, sheetName):
    """Loads the respective row from the Excel file for
    the given keyword.


    Parameters
    ----------              
    keyword: str
        Keyword to search Excel file
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """   
    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetName);
    for i in range(0, sheet.nrows): 
        if sheet.cell_value(i, 0).startswith(keyword):
            return i
    
    print("WARNING: Row starting with keyword", keyword, "not found!")
    return 0
    



    
#Returns number of zones in the swimming pool
def countZones(filePath, sheetNameAreas):
    """Counts the number of standard zones (no pool zones) of the given 
    swimming pool.


    Parameters
    ----------          
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """   
    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetNameAreas);
    
    numZones=0
    for i in range(0, 3):
        for k in range(0, sheet.ncols):
            if sheet.cell_value(i, k).startswith("Zone 1"):
                for m in range(k, sheet.ncols):
                    if sheet.cell_value(i, m).startswith("Zone"):
                        numZones+=1
                return numZones                   
            
            
            
            
            
def getPoolData(filePath, sheetNameAreas):
    """Loads additional data for the pools from the Excel file and safes
    them to a list with the structure
    [DESIGNATION, AREA, FLOOR WITH EARTH CONTACT, WATER VOLUME, WATER TEMPERATURE]

    Parameters
    ----------          
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """   
    wb = xlrd.open_workbook(filePath)
    sheet = wb.sheet_by_name(sheetNameAreas)    
    numPools=countPools(filePath, sheetNameAreas)
    pools=[]
    startCol = getCol("SB", filePath, sheetNameAreas)

    
    for col in range(numPools):
        
        pools.append([])
        startRow = 2
        pools[col].append(sheet.cell_value(startRow, startCol))
        startRow = 4
        for n in range(0,4):
            pools[col].append(sheet.cell_value(startRow, startCol))
            startRow+=1
        startCol+=1
            
    return pools





def getPoolDataInDict(ZoneId, filePath, sheetNameAreas):
    """Loads additional data for the pools from the Excel file and saves
    them to a dictionary with the structure
    [DESIGNATION, AREA, FLOOR WITH EARTH CONTACT, WATER VOLUME, WATER TEMPERATURE]

    Parameters
    ----------          
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
        
    ZoneId: int or ("SUM")
        Auxilary parameter to indicate the respective zone
                 
    """   
    
    if (isinstance(ZoneId, int) == True):
        if ZoneId < 8:
            return 0.0
    if ZoneId == 8:
        PoolName = "SB"
    elif ZoneId == 9:
        PoolName = "MZB"
    elif ZoneId == 10:
        PoolName = "KB"
    elif ZoneId == 11:
        PoolName = "NSB"
    elif ZoneId == 12:
        PoolName = "SPB"
    elif ZoneId == 13:
        PoolName = "FB1"
    elif ZoneId == 14:
        PoolName = "FB2"
    elif ZoneId == 15:
        PoolName = "FB3"
    elif ZoneId == 16:
        PoolName = "FB4"
    elif ZoneId == "SUM":
        PoolName = "SUM"
        
    wb = xlrd.open_workbook(filePath)
    sheet = wb.sheet_by_name(sheetNameAreas)    
    numPools=countPools(filePath, sheetNameAreas)
    startCol = getCol("SUM", filePath, sheetNameAreas)
    startRow = 2
    
    additionalInfo = dict()
    
    for pools in range(numPools + 1):
        pool = sheet.cell_value(startRow, startCol + pools)
        additionalInfo[str(pool)] = dict()
        
        for data in range(4):
            colName = sheet.cell_value(startRow + 2 + data, startCol - 2)
            additionalInfo[pool][str(colName)] = sheet.cell_value(startRow + 2 + data, startCol + pools)
            
    return additionalInfo[PoolName]
        
   



def countPools(filePath, sheetNameAreas):
    """Counts the number of pools of the given 
    swimming pool.

    Parameters
    ----------          
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """   

    wb = xlrd.open_workbook(filePath);
    sheet = wb.sheet_by_name(sheetNameAreas);    
    pools = 0
    startCol = getCol("SB", filePath, sheetNameAreas)
    
    for n in range(sheet.ncols):
        try:
            if sheet.cell_value(2, startCol) == "":
                return pools
            else:
                pools+=1
                startCol+=1
        except IndexError:
            return pools


    


def getKeyword(inKey, filePath, sheetName):
    """Returns a keyword for a given expression.
    Parameters
    ----------   
    inKey : str
        Input keyword       
    filePath: str
        Path to Excel File
        
    sheetNameAreas: str
        Name of the sheet within the Excel File that contains the element areas
                 
    """ 
    
    #PoolNames
    if (inKey == "SB"):
        return "Schwimmerbecken"
    elif (inKey == "MZB"):
        return "Mehrzweckbecken"
    elif (inKey == "NSB"):
        return "Nichtschwimmerbecken"
    elif (inKey == "SPB"):
        return "Springerbecken"
    elif (inKey == "KB"):
        return "Kleinkinderbecken"
    elif (inKey == "VB"):
        return "Variobecken"    
    elif (inKey == "FB1"):
        return "Freiformbecken 1"
    elif (inKey == "FB2"):
        return "Freiformbecken 2"
    elif (inKey == "FB3"):
        return "Freiformbecken 3"
    elif (inKey == "FB4"):
        return "Freiformbecken 4" 
    
    #Envelope Surfaces in Excel File
    elif (inKey == "OuterWall"):
        return "Outer walls and cardinal"
    elif (inKey == "Window"):
        return "Transparent elements in"
    elif (inKey == "Rooftop"):
        return "Roof"
    elif (inKey == "GroundFloor"):
        return "Ground floor"  

    else:
        print("Keyword for Key", inKey, "not found in", sheetName, "of Excel file",
              filePath)
        return inKey
 
"""
ZoneId = 16
filePath='C:/Users/schmi/.conda/envs/py37/lib/site-packages/teaser/examples/2020-11-04_Hüllflächen_Zonen_Shells_of_Zones_tsc.xlsx'
sheetNameAreas='Hüllflächen, Himmelsricht.'
Test = getPoolDataInDict(ZoneId ,filePath, sheetNameAreas)
Number = countPools(filePath, sheetNameAreas)

print(Test)
"""