# ccma_artists.json

## Add Column

## Add Node/Literal
#### Literal Node: `http://vocab.getty.edu/aat/300404672`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`

#### Literal Node: `http://vocab.getty.edu/aat/300404670`
Literal Type: ``
<br/>Language: ``
<br/>isUri: `true`


## PyTransforms
#### _ConstituentURI_
From column: __Artist_ID_
``` python
return "constituent/"+getValue("_Artist_ID")
```

#### _NameLabel_
From column: _Display_Name_
``` python
return getValue("Display_Name")
```

#### _NameURI_
From column: _Last_Name_
``` python
return getValue("ConstituentURI")+"/name"
```

#### _SortNameURI_
From column: _Nat_Culture_L2_
``` python
return getValue("ConstituentURI")+"/sort_name"
```

#### _DeathURI_
From column: _Suffix_
``` python
if getValue("End_Date_Disp"):
    return getValue("ConstituentURI")+"/death"
else:
    return ""
```

#### _DeathDateEnd_
From column: _End_Date_Disp_
``` python
return getValue("End_Date_Disp")
```

#### _DisplayDateCopy_
From column: _Disp_Maker_Life_
``` python
return getValue("Disp_Maker_Life")
```

#### _BirthDateEnd_
From column: _Start_Date_Disp_
``` python
return getValue("Start_Date_Disp")
```

#### _BirthURI_
From column: _ConstituentURI_
``` python
if getValue("Start_Date_Disp"):
    return getValue("ConstituentURI")+"/birth"
else:
    return ""
```

#### _BirthDateURI_
From column: _BirthURI_
``` python
if getValue("Start_Date_Disp"):
    return getValue("ConstituentURI")+"/birth/date"
else:
    return ""
```

#### _DeathDateURI_
From column: _DeathURI_
``` python
if getValue("End_Date_Disp"):
    return getValue("ConstituentURI")+"/death/date"
else:
    return ""
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _BirthDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span2`|
| _BirthDateURI_ | `uri` | `crm:E52_Time-Span2`|
| _BirthURI_ | `uri` | `crm:E63_Beginning_of_Existence1`|
| _ConstituentURI_ | `uri` | `crm:E39_Actor1`|
| _DeathDateEnd_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| _DeathDateURI_ | `uri` | `crm:E52_Time-Span1`|
| _DeathURI_ | `uri` | `crm:E64_End_of_Existence1`|
| _Disp_Maker_Life_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _DisplayDateCopy_ | `rdfs:label` | `crm:E52_Time-Span2`|
| _Display_Name_ | `rdf:value` | `crm:E82_Actor_Appellation1`|
| _End_Date_Disp_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _NameLabel_ | `rdfs:label` | `crm:E39_Actor1`|
| _NameURI_ | `uri` | `crm:E82_Actor_Appellation1`|
| _SortNameURI_ | `uri` | `crm:E82_Actor_Appellation2`|
| _Sort_Name_ | `rdf:value` | `crm:E82_Actor_Appellation2`|
| _Start_Date_Disp_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span2`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E39_Actor1` | `crm:P92i_was_brought_into_existence_by` | `crm:E63_Beginning_of_Existence1`|
| `crm:E39_Actor1` | `crm:P93i_was_taken_out_of_existence_by` | `crm:E64_End_of_Existence1`|
| `crm:E39_Actor1` | `crm:P131_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation2`|
| `crm:E39_Actor1` | `crm:P1_is_identified_by` | `crm:E82_Actor_Appellation1`|
| `crm:E63_Beginning_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span2`|
| `crm:E64_End_of_Existence1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E82_Actor_Appellation1` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404670`|
| `crm:E82_Actor_Appellation2` | `crm:P2_has_type` | `http://vocab.getty.edu/aat/300404672`|
