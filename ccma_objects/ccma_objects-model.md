# ccma_objects.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300264237`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/ulan/500311505`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ObjectURI_
From column: _objects / embark_ID_
``` python
return "object/"+getValue("embark_ID")
```

#### _TitleURI_
From column: _objects / Obj_Title_
``` python
if getValue("Disp_Title")!="Untitled":
    return UM.uri_from_fields("thesauri/title/",getValue("Disp_Title"))
else:
    return ""
```

#### _TitleLabel_
From column: _objects / Disp_Title_
``` python
return getValue("Disp_Title")
```

#### _AlternateTitleURI_
From column: _objects / TitleLabel_
``` python
if getValue("Alt_Title"):
    return getValue("ObjectURI")+"/alt_title"
else:
    return ""
```

#### _TypeAssignmentURI_
From column: _objects / Alt_Title_
``` python
if getValue("Disp_Obj_Type"):
    return getValue("ObjectURI")+"/classification"
else:
    return ""
```

#### _TypeURI_
From column: _objects / TypeAssignmentURI_
``` python
if getValue("Disp_Obj_Type"):
    return "thesauri/classification/"+getValue("Disp_Obj_Type").lower()
else:
    return ""
```

#### _DimensionStringURI_
From column: _objects / Support_
``` python
if getValue("Disp_Dimen"):
    return getValue("ObjectURI")+"/dimension"
else:
    return ""
```

#### _ProductionURI_
From column: _objects / Edition_
``` python
if getValue("Disp_Create_DT"):
    return getValue("ObjectURI")+"/production"
else:
    return ""
```

#### _TimeSpanURI_
From column: _objects / ProductionURI_
``` python
if getValue("Disp_Create_DT"):
    return getValue("ObjectURI")+"/production/timespan"
else:
    return ""
```

#### _MediumTextURI_
From column: _objects / Creation_Place2_
``` python
if getValue("Disp_Medium"):
    return getValue("ObjectURI")+"/medium"
else:
    return ""
```

#### _MediumURI_
From column: _objects / Disp_Medium_
``` python
if getValue("Medium"):
    return UM.uri_from_fields("thesauri/material/",getValue("Medium"))
else:
    return ""
```

#### _URLLabel_
From column: _objects / URL_
``` python
return getValue("URL")
```

#### _OwnerURI_
From column: _objects / ObjectURI_
``` python
return "data.americanartcollaborative.org/ccma"
```

#### _OwnerLabel_
From column: _objects / OwnerURI_
``` python
return "Colby College Museum of Art"
```

#### _PhyObjURI_
From column: _objects / Period_
``` python
return getValue("ObjectURI")+"/physical_object"
```

#### _DepartmentURI_
From column: _objects / PhyObjURI_
``` python
return UM.uri_from_fields("thesauri/department/",getValue("Department"))
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Alt_Title_ | `rdf:value` | `crm:E35_Title2`|
| _AlternateTitleURI_ | `uri` | `crm:E35_Title2`|
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentURI_ | `uri` | `crm:E74_Group1`|
| _DimensionStringURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _Disp_Create_DT_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Disp_Dimen_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Disp_Medium_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _Disp_Obj_Type_ | `rdfs:label` | `crm:E55_Type1`|
| _Disp_Title_ | `rdf:value` | `crm:E35_Title1`|
| _IIIF_URL_ | `uri` | `crm:E38_Image1`|
| _Medium_ | `skos:prefLabel` | `crm:E57_Material1`|
| _MediumTextURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _MediumURI_ | `uri` | `crm:E57_Material1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _PhyObjURI_ | `uri` | `crm:E19_Physical_Object1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _TypeAssignmentURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _URL_ | `uri` | `foaf:Document1`|
| _URLLabel_ | `rdfs:label` | `foaf:Document1`|
| __Disp_End_Date_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| __Disp_Start_Dat_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P41i_was_classified_by` | `crm:E17_Type_Assignment1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object2`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title2`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P52_has_current_owner` | `crm:E40_Legal_Body1`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300264237`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500311505`|
