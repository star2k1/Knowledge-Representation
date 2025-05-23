# HW3 - Knowledge Representation

**Course:** Knowledge Representation  
**Task Description:** This homework focuses on comparing responses from a large language model (Claude Sonnet 4) with formal queries using LogicTools. The goal is to assess how well the model aligns with structured logic-based systems in handling Estonian knowledge queries.

---

# Test 1 - Lakes of Pärnumaa

## Claude Sonnet 4 Results

**Prompt:**  
`Kumb järv on suurem, kas Nigula või Tõhela?`

**Claude's Answer:**  
Nigula järv on suurem kui Tõhela järv.

Nigula järv asub Pärnumaal Häädemeeste vallas ja on üks Eesti suuremaid järvi, selle pindala on umbes 170 hektarit. Tõhela järv on märksa väiksem - see asub samuti Pärnumaal ja on osa Nigula looduskaitsealast, kuid tema pindala on oluliselt väiksem.

## Logictools

**Rule and query:**

```lisp
["forall", ["X","Y","X1","Y1"],
  [
    [["Area","X","X1"], "&", ["Area","Y","Y1"], "&", [">","Y1","X1"]],
    "=>",
    ["larger","X","Y"]
  ]
]


["~larger","Nigula https://et.wikipedia.org/wiki/Nigula_j%C3%A4rv","T\u00f5hela https://et.wikipedia.org/wiki/T%C3%B5hela_j%C3%A4rv"]
```

**Response:**

```lisp

{"result": "proof found",

"answers": [
{
"proof":
[
[1, ["in", "frm_15"], [["-$greater","?:X","?:Y"], ["-Area","?:Z","?:X"], ["-Area","?:U","?:Y"], ["larger","?:U","?:Z"]]],
[2, ["in", "frm_4"], [["Area","Tõhela https://et.wikipedia.org/wiki/T%C3%B5hela_j%C3%A4rv",407.300000]]],
[3, ["mp", [1,1], 2], [["-$greater",407.300000,"?:X"], ["-Area","?:Y","?:X"], ["larger","?:Y","Tõhela https://et.wikipedia.org/wiki/T%C3%B5hela_j%C3%A4rv"]]],
[4, ["in", "frm_12"], [["Area","Nigula https://et.wikipedia.org/wiki/Nigula_j%C3%A4rv",17.900000]]],
[5, ["in", "frm_16"], [["-larger","Nigula https://et.wikipedia.org/wiki/Nigula_j%C3%A4rv","Tõhela https://et.wikipedia.org/wiki/T%C3%B5hela_j%C3%A4rv"]]],
[6, ["mp", [3,1], 4, 5], false]
]}
]}
```

.
