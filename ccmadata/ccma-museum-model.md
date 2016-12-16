# ccma-objects_artists_exhibs.json

## Add Column

## Add Node/Literal
#### Literal Node: `aat:300266036`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300263534`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300312355`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300379842`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `http://vocab.getty.edu/aat/300266036`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300263534`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `http://vocab.getty.edu/aat/300312355`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300379842`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404651`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404652`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _man_made_object_uri_
From column: _objects / Style_
``` python
return getValue("Style")
```

#### _Display_dimension_uri_
From column: _objects / Disp_Dimen_
``` python
return getValue("row_uri")+"/"+"dimension_string"
```

#### _MediumURI_
From column: _objects / Disp_Medium_
``` python
return getValue("row_uri") + '/medium/'
```

#### _Disp_Title_URI_
From column: _objects / Disp_Title_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Disp_Title"))
```

#### _Department_URI_
From column: _objects / Department_
``` python
return UM.uri_from_fields("thesauri/department/",getValue("Department"))
```

#### _row_uri_
From column: _objects / embark_ID_
``` python
return "object/"+getValue("embark_ID")
```

#### _disp_access_no_uri_
From column: _objects / Disp_Access_No_
``` python
return UM.uri_from_fields(getValue("row_uri")+"/",getValue("Disp_Access_No"))
```

#### _disp_create_date_uri_
From column: _objects / Disp_Create_DT_
``` python
return UM.uri_from_fields(getValue("row_uri")+"/",getValue("Disp_Create_DT"))
```

#### _disp_obj_type_uri_
From column: _objects / Disp_Obj_Type_
``` python
return UM.uri_from_fields("thesauri/object_type/",getValue("Disp_Obj_Type"))
```

#### _artist_uri_
From column: _objects / Artist_Split / Values_
``` python
return UM.uri_from_fields("thesauri/artist/",getValue("Values"))
```

#### _imagepath_uri_
From column: _objects / Images / ImagePath_
``` python
return getValue("ImagePath")
```

#### _url_uri_
From column: _objects / URL_
``` python
return getValue("URL")
```

#### _fnam_uri_
From column: _artists / First_Name_
``` python
return UM.uri_from_fields("thesauri/first_name/",getValue("First_Name"))
```

#### _lname_uri_
From column: _artists / Last_Name_
``` python
return UM.uri_from_fields("thesauri/last_name/",getValue("Last_Name"))
```

#### _display_name_uri_
From column: _artists / Display_Name_
``` python
return UM.uri_from_fields("thesauri/display_name/",getValue("Display_Name"))
```

#### _nationality_uri_
From column: _artists / Nat_Culture_L2_
``` python
return  UM.uri_from_fields("thesauri/nationality/",getValue("Nat_Culture_L2"))
```

#### _start_date_uri_
From column: _artists / Start_Date_Disp_
``` python
return UM.uri_from_fields("artist/"+ getValue("_Artist_ID")+"/end_date/"
,getValue("Start_Date_Disp"))
```

#### _end_date_uri_
From column: _artists / End_Date_Disp_
``` python
return UM.uri_from_fields("artist/"+ getValue("_Artist_ID")+"/end_date/"
,getValue("End_Date_Disp"))
```

#### _collection_name_
From column: _objects / Department_
``` python
return getValue("Department")
```

#### _accession_duplicate_
From column: _objects / Disp_Access_No_
``` python
return getValue("Disp_Access_No")
```

#### _display_date_duplicate_
From column: _objects / Disp_Title_
``` python
return getValue("Disp_Title")
```

#### _display_name_duplicate_
From column: _artists / Display_Name_
``` python
return getValue("Display_Name")
```

#### _display_name_uri_duplicate_
From column: _artists / display_name_uri_
``` python
return UM.uri_from_fields("thesauri/display_name/",getValue("Display_Name"))
```

#### _display_main_duplicate_
From column: _artists / display_name_uri_duplicate_
``` python
return getValue("Display_Name")
```

#### _physical_object_uri_
From column: _objects / collection_name_
``` python
return getValue("row_uri")+"/physical_object"
```

#### _production_uri_
From column: _objects / physical_object_uri_
``` python
return getValue("row_uri")+"/production_uri"
```

#### _display_aritst_mmo_
From column: _objects / Sort_Artist_
``` python
x,y = getValue("Sort_Artist").split(',')
return y.strip(' ') + ' ' + x
```

#### _temp_artist_uri_
From column: _objects / display_aritst_mmo_
``` python
return UM.uri_from_fields("artist/uri/",getValue("display_aritst_mmo"))
```

#### _artist_name_uri_
From column: _artists / display_name_duplicate_
``` python
return UM.uri_from_fields("artist/uri/",getValue("Display_Name"))
```

#### _end_existance_uri_
From column: _artists / end_date_uri_
``` python
return getValue("artist_name_uri") + "/end_existance"
```

#### _begining_existance_uri_
From column: _artists / start_date_uri_
``` python
return getValue("artist_name_uri") + "/begining_existance"
```

#### _type1_uri_
From column: _artists / fnam_uri_
``` python
return UM.uri_from_fields("thesauri/first_name/",getValue("First_Name"))
```

#### _type2_uri_
From column: _artists / lname_uri_
``` python
return UM.uri_from_fields("thesauri/last_name/",getValue("Last_Name"))
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _Department_URI_ | `uri` | `crm:E74_Group1`|
| _Disp_Access_No_ | `rdfs:label` | `crm:E42_Identifier1`|
| _Disp_Create_DT_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Disp_Dimen_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Disp_Medium_ | `skos:prefLabel` | `crm:E57_Material1`|
| _Disp_Obj_Type_ | `rdfs:label` | `crm:E55_Type2`|
| _Disp_Title_ | `rdf:value` | `crm:E35_Title1`|
| _Disp_Title_URI_ | `uri` | `crm:E35_Title1`|
| _Display_Name_ | `rdf:value` | `crm:E82_Actor_Appellation3`|
| _Display_dimension_uri_ | `uri` | `crm:E33_Linguistic_Object1`|
| _End_Date_Disp_ | `rdfs:label` | `crm:E52_Time-Span3`|
| _First_Name_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _ImagePath_ | `rdfs:label` | `crm:E38_Image1`|
| _Last_Name_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _Medium_ | `skos:prefLabel` | `crm:E57_Material2`|
| _MediumURI_ | `uri` | `crm:E57_Material1`|
| _Nat_Culture_L2_ | `rdfs:label` | `crm:E74_Group2`|
| _Start_Date_Disp_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _URL_ | `rdfs:label` | `foaf:Document1`|
| __Disp_End_Date_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| __Disp_Start_Dat_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _accession_duplicate_ | `rdf:value` | `crm:E42_Identifier1`|
| _artist_name_uri_ | `uri` | `crm:E39_Actor1`|
| _begining_existance_uri_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _collection_name_ | `rdfs:label` | `crm:E19_Physical_Object1`|
| _disp_access_no_uri_ | `uri` | `crm:E42_Identifier1`|
| _disp_create_date_uri_ | `uri` | `crm:E52_Time-Span1`|
| _disp_obj_type_uri_ | `uri` | `crm:E55_Type2`|
| _display_aritst_mmo_ | `rdfs:label` | `crm:E39_Actor2`|
| _display_date_duplicate_ | `rdfs:label` | `crm:E22_Man-Made_Object1`|
| _display_main_duplicate_ | `rdfs:label` | `crm:E39_Actor1`|
| _display_name_duplicate_ | `rdf:value` | `crm:E82_Actor_Appellation4`|
| _display_name_uri_ | `uri` | `crm:E82_Actor_Appellation3`|
| _display_name_uri_duplicate_ | `uri` | `crm:E82_Actor_Appellation4`|
| _end_date_uri_ | `uri` | `crm:E52_Time-Span3`|
| _end_existance_uri_ | `uri` | `crm:E64_End_of_Existence1`|
| _fnam_uri_ | `uri` | `crm:E82_Actor_Appellation1`|
| _imagepath_uri_ | `uri` | `crm:E38_Image1`|
| _lname_uri_ | `uri` | `crm:E82_Actor_Appellation2`|
| _nationality_uri_ | `uri` | `crm:E74_Group2`|
| _physical_object_uri_ | `uri` | `crm:E19_Physical_Object1`|
| _production_uri_ | `uri` | `crm:E12_Production1`|
| _row_uri_ | `uri` | `crm:E22_Man-Made_Object1`|
| _start_date_uri_ | `uri` | `crm:E52_Time-Span2`|
| _temp_artist_uri_ | `uri` | `crm:E39_Actor2`|
| _type1_uri_ | `uri` | `crm:E55_Type1`|
| _type2_uri_ | `uri` | `crm:E55_Type3`|
| _url_uri_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor2`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material2`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300266036`|
| `crm:E35_Title1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation4`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group2`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300312355`|
| `crm:E55_Type1` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404651`|
| `crm:E55_Type3` | `skos:broadMatch` | `xsd:http://vocab.getty.edu/aat/300404652`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span3`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300263534`|
| `crm:E74_Group2` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300379842`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `crm:E55_Type1`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `crm:E55_Type3`|
| `crm:E82_Actor_Appellation4` | `crm:P2_has_type` | `xsd:http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation4` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| `crm:E82_Actor_Appellation4` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation3`|
| `crm:E82_Actor_Appellation4` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
