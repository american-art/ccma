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

#### Literal Node: `http://vocab.getty.edu/aat/300263534`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://data.americanartcollaborative.org/ccma`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300179869`
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
if getValue("Disp_Create_DT") or getValue("_Artist_ID"):
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
return "http://data.americanartcollaborative.org/ccma"
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

#### _PrefIdURI_
From column: _objects / embark_ID_
``` python
return getValue("ObjectURI")+"/pref_id"
```

#### _ID_Label_
From column: _objects / embark_ID_
``` python
return getValue("embark_ID")
```

#### _ConstituentURI_
From column: _objects / _Artist_ID_
``` python
return "constituent/"+getValue("_Artist_ID")
```

#### _AccessionNoURI_
From column: _objects / OwnerLabel_
``` python
return getValue("ObjectURI")+"/acc_no"
```

#### _AccNoType_
From column: _objects / Disp_Access_No_
``` python
return "http://vocab.getty.edu/aat/300312355"
```

#### _Medium_clean_
From column: _objects / Medium_
``` python
return getValue("Medium").strip().lower()
```

#### _StartDateFormatted_
From column: _objects / _Disp_Start_Dat_
``` python
if getValue("_Disp_Start_Dat"):
    return "01-01-" + getValue("_Disp_Start_Dat")
else:
    return ""
```

#### _EndDateFormatted_
From column: _objects / _Disp_End_Date_
``` python
if getValue("_Disp_End_Date"):
    return "12-31-" + getValue("_Disp_End_Date")
else:
    return ""
```

#### _DateLabel_
From column: _objects / Disp_Create_DT_
``` python
return getValue("StartDateFormatted")+" to "+getValue("EndDateFormatted")
```

#### _ImagePathEscaped_
From column: _objects / Images / ImagePath_
``` python
path = getValue("ImagePath")
path = path.split(",")
path = "\,".join(path)
return path
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _AccNoType_ | `uri` | `crm:E55_Type2`|
| _AccessionNoURI_ | `uri` | `crm:E42_Identifier2`|
| _Alt_Title_ | `rdf:value` | `crm:E35_Title2`|
| _AlternateTitleURI_ | `uri` | `crm:E35_Title2`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DateLabel_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _DepartmentURI_ | `uri` | `crm:E74_Group1`|
| _DimensionStringURI_ | `uri` | `crm:E33_Linguistic_Object1`|
| _Disp_Access_No_ | `rdf:value` | `crm:E42_Identifier2`|
| _Disp_Dimen_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Disp_Medium_ | `rdf:value` | `crm:E33_Linguistic_Object2`|
| _Disp_Obj_Type_ | `rdfs:label` | `crm:E55_Type1`|
| _Disp_Title_ | `rdf:value` | `crm:E35_Title1`|
| _EndDateFormatted_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _ID_Label_ | `rdfs:label` | `crm:E42_Identifier1`|
| _ImagePath_ | `uri` | `crm:E38_Image1`|
| _MediumTextURI_ | `uri` | `crm:E33_Linguistic_Object2`|
| _MediumURI_ | `uri` | `crm:E57_Material1`|
| _Medium_clean_ | `skos:prefLabel` | `crm:E57_Material1`|
| _ObjectURI_ | `uri` | `crm:E22_Man-Made_Object1`|
| _OwnerLabel_ | `rdfs:label` | `crm:E40_Legal_Body1`|
| _OwnerURI_ | `uri` | `crm:E40_Legal_Body1`|
| _PhyObjURI_ | `uri` | `crm:E19_Physical_Object1`|
| _PrefIdURI_ | `uri` | `crm:E42_Identifier1`|
| _ProductionURI_ | `uri` | `crm:E12_Production1`|
| _StartDateFormatted_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _TimeSpanURI_ | `uri` | `crm:E52_Time-Span1`|
| _TitleLabel_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _TitleURI_ | `uri` | `crm:E35_Title1`|
| _TypeAssignmentURI_ | `uri` | `crm:E17_Type_Assignment1`|
| _TypeURI_ | `uri` | `crm:E55_Type1`|
| _URL_ | `uri` | `foaf:Document1`|
| _URLLabel_ | `rdfs:label` | `foaf:Document1`|
| _embark_ID_ | `rdf:value` | `crm:E42_Identifier1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P108i_was_produced_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E17_Type_Assignment1` | `crm:P42_assigned` | `crm:E55_Type1`|
| `crm:E17_Type_Assignment1` | `crm:P21_had_general_purpose` | `http://vocab.getty.edu/aat/300179869`|
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
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier2`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300266036`|
| `crm:E33_Linguistic_Object2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300264237`|
| `crm:E35_Title1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E40_Legal_Body1` | `skos:exactMatch` | `http://vocab.getty.edu/ulan/500311505`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E42_Identifier2` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E74_Group1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300263534`|
| `crm:E74_Group1` | `crm:P107i_is_current_or_former_member_of` | `http://data.americanartcollaborative.org/ccma`|
