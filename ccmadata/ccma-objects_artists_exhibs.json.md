## ccma-objects_artists_exhibs.json

### PyTransforms
#### _ConstituentURI_
From column: _objects / embark_ID_
>``` python
return getValue("embark_ID")
```

#### _DisplayAccessNoURI_
From column: _objects / Disp_Access_No_
>``` python
if getValue("Disp_Access_No") == 'NULL':
    return " "
else:
    return getValue("Disp_Access_No")
```

#### _DisplayCreateDateURI_
From column: _objects / Disp_Create_DT_
>``` python
if getValue("Disp_Create_DT") == 'NULL':
    return " "
else:
    return getValue("Disp_Create_DT")
```

#### _DisplayStartDateURI_
From column: _objects / _Disp_Start_Dat_
>``` python
if getValue("_Disp_Start_Dat") == 'NULL':
    return " "
else:
    return getValue("_Disp_Start_Dat")
```

#### _DisplayEndDateURI_
From column: _objects / _Disp_End_Date_
>``` python
if getValue("_Disp_End_Date") == 'NULL':
    return " "
else:
    return getValue("_Disp_End_Date")
```

#### _DisplayTitleURI_
From column: _objects / Disp_Title_
>``` python
if getValue("Disp_Title") == 'NULL':
    return " "
else:
    return getValue("Disp_Title")
```

#### _AltTitleURI_
From column: _objects / Alt_Title_
>``` python
if getValue("Alt_Title") == 'NULL':
    return " "
else:
    return getValue("Alt-Title")
```

#### _ExhibitionNameURI_
From column: _exhibitions / Exhibition_Name_
>``` python
if getValue("Exhibition_Name") == 'NULL':
    return " "
else:
    return getValue("Exhibition_Name")
```

#### _ExhibStartDateURI_
From column: _exhibitions / Start_Date_
>``` python
if getValue("Start_Date") == 'NULL':
    return " "
else:
    return getValue("Start_Date")
```

#### _ExhibEndDateURI_
From column: _exhibitions / End_Date_
>``` python
if getValue("End_Date") == 'NULL':
    return " "
else:
    return getValue("End_Date")
```

#### _EmbarkIdURI_
From column: _exhibitions / embark_ID_
>``` python
if getValue("embark_ID") == 'NULL':
    return " "
else:
    return getValue("embark_ID")
```

#### _SortNameURI_
From column: _artists / Sort_Name_
>``` python
if getValue("Sort_Name") == 'NULL':
    return " "
else:
    return getValue("Sort_Name")
```

#### _DisplayNameURI_
From column: _artists / Display_Name_
>``` python
if getValue("Display_Name") == 'NULL':
    return " "
else:
    return getValue("Display_Name")
```

#### _CultureURI_
From column: _artists / Nat_Culture_L2_
>``` python
if getValue("Nat_Culture_L2") == 'NULL':
    return " "
else:
    return getValue("Nat_Culture_L2")
```

#### _LifespanURI_
From column: _artists / Disp_Maker_Life_
>``` python
if getValue("Disp_Maker_Life") == 'NULL':
    return " "
else:
    return getValue("Disp_Maker_Life")
```

#### _LastNameURI_
From column: _artists / Last_Name_
>``` python
if getValue("Last_Name") == 'NULL':
    return " "
else:
    return getValue("Last_Name")
```

#### _FirstNameURI_
From column: _artists / First_Name_
>``` python
if getValue("First_Name") == 'NULL':
    return " "
else:
    return getValue("First_Name")
```

#### _StartDateURI_
From column: _artists / Start_Date_Disp_
>``` python
if getValue("Start_Date_Disp") == 'NULL':
    return " "
else:
    return getValue("Start_Date_Disp")
```

#### _EndDateURI_
From column: _artists / End_Date_Disp_
>``` python
if getValue("End_Date_Disp") == 'NULL':
    return " "
else:
    return getValue("End_Date_Disp")
```

#### _ArtistCodeURI_
From column: _artists / Artist_Code_
>``` python
if getValue("Artist_Code") == 'NULL':
    return " "
else:
    return getValue("Artist_Code")
```

#### _BiographyURI_
From column: _artists / Biography_
>``` python
if getValue("Biography") == 'NULL':
    return " "
else:
    return getValue("Biography")
```

#### _ArtistIdURI_
From column: _artists / _Artist_ID_
>``` python
if getValue("_Artist_ID") == 'NULL':
    return " "
else:
    return getValue("_Artist_ID")
```

#### _RemarksURI_
From column: _objects / Remarks_
>``` python
if getValue("Remarks") == 'NULL':
    return " "
else:
    return getValue("Remarks")
```


### Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _ArtistCodeURI_ | `uri` | `crm:E42_Identifier3`|
| _ArtistIdURI_ | `uri` | `crm:E39_Actor1`|
| _BiographyURI_ | `uri` | `crm:E31_Document1`|
| _ConstituentURI_ | `uri` | `crm:E35_Title1`|
| _CultureURI_ | `uri` | `crm:E74_Group1`|
| _DisplayAccessNoURI_ | `uri` | `crm:E42_Identifier1`|
| _DisplayCreateDateURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _DisplayEndDateURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _DisplayNameURI_ | `uri` | `crm:E15_Identifier_Assignment2`|
| _DisplayStartDateURI_ | `uri` | `crm:E63_Beginning_of_Existence2`|
| _DisplayTitleURI_ | `crm:P102_has_title` | `crm:E35_Title1`|
| _EmbarkIdURI_ | `uri` | `crm:E42_Identifier2`|
| _EndDateURI_ | `uri` | `crm:E69_Death1`|
| _ExhibEndDateURI_ | `uri` | `crm:E50_Date2`|
| _ExhibStartDateURI_ | `uri` | `crm:E50_Date1`|
| _ExhibitionNameURI_ | `uri` | `crm:E35_Title2`|
| _FirstNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _LastNameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _LifespanURI_ | `uri` | `crm:E52_Time-Span3`|
| _SortNameURI_ | `uri` | `crm:E15_Identifier_Assignment1`|
| _StartDateURI_ | `uri` | `crm:E67_Birth1`|


### Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E35_Title1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E35_Title1` | `crm:P4_has_time-span` | `crm:E52_Time-Span7`|
| `crm:E39_Actor1` | `crm:P100i_died_in` | `crm:E69_Death1`|
| `crm:E39_Actor1` | `crm:P107i_is_current_or_former_member_of` | `crm:E74_Group1`|
| `crm:E39_Actor1` | `crm:P129i_is_subject_of` | `crm:E31_Document1`|
| `crm:E39_Actor1` | `crm:P140i_was_attributed_by` | `crm:E15_Identifier_Assignment1`|
| `crm:E39_Actor1` | `crm:P140i_was_attributed_by` | `crm:E15_Identifier_Assignment2`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E42_Identifier3`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation3`|
| `crm:E39_Actor1` | `crm:P4_has_time-span` | `crm:E52_Time-Span3`|
| `crm:E39_Actor1` | `crm:P98i_was_born` | `crm:E67_Birth1`|
| `crm:E52_Time-Span4` | `crm:P4i_is_time-span_of` | `crm:E63_Beginning_of_Existence1`|
| `crm:E52_Time-Span5` | `crm:P4i_is_time-span_of` | `crm:E63_Beginning_of_Existence2`|
| `crm:E52_Time-Span6` | `crm:P4i_is_time-span_of` | `crm:E64_End_of_Existence1`|
| `crm:E52_Time-Span8` | `crm:P1_is_identified_by` | `crm:E50_Date1`|
| `crm:E52_Time-Span8` | `crm:P1_is_identified_by` | `crm:E50_Date2`|
| `crm:E78_Collection1` | `crm:P102_has_title` | `crm:E35_Title2`|
| `crm:E78_Collection1` | `crm:P1_is_identified_by` | `crm:E42_Identifier2`|
| `crm:E78_Collection1` | `crm:P4_has_time-span` | `crm:E52_Time-Span8`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation1`|
| `crm:E82_Actor_Appellation3` | `crm:P106_is_composed_of` | `crm:E82_Actor_Appellation2`|
