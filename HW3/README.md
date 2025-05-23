# 🧠 HW3 - Knowledge Representation

**Course:** Knowledge Representation  
**Task Description:** This homework focuses on comparing responses from a large language model (Claude Sonnet 4) with formal queries using LogicTools. The goal is to assess how well the model aligns with structured logic-based systems in handling Estonian knowledge queries.

---

# 🧪 Test 1 - Lakes of Pärnumaa

## 🤖 Claude Sonnet 4 Results

**Prompt:**  
`Kumb järv on suurem, kas Nigula või Tõhela?`

**Claude's Answer:**  
Nigula järv on suurem kui Tõhela järv.

Nigula järv asub Pärnumaal Häädemeeste vallas ja on üks Eesti suuremaid järvi, selle pindala on umbes 170 hektarit. Tõhela järv on märksa väiksem - see asub samuti Pärnumaal ja on osa Nigula looduskaitsealast, kuid tema pindala on oluliselt väiksem.
(_Incorrect according to LogicTools_)

## 🧮 Logictools

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

**In words**

Nigula järv ei ole suurem kui Tõhela. **Tõhela** is the larger lake.

# 🏝️ Test 2 - Smallest Island

## 🤖 Claude Sonnet 4 Results

**Prompt:**  
`Milline saar on kõige väiksem, Kõrksaar, Rammu saar või Pedassaar?`

**Claude's Answer:**  
Kõige väiksem neist kolmest on **Kõrksaar**.

Kõrksaar on väike saar Eesti rannikul, mille pindala on umbes 0,5 hektarit. Rammu saar on märksa suurem (umbes 4,6 km²) ja Pedassaar on samuti suurem kui Kõrksaar, kuigi väiksem kui Rammu saar.(_Incorrect according to LogicTools_)

## 🧮 Logictools

**Rule and query:**

```lisp
["forall", ["A", "B", "C", "A1", "B1", "C1"], [[["Area", "A", "A1"], "&", ["Area", "B", "B1"], "&", ["Area", "C", "C1"], "&", ["$greater", "B1", "A1"], "&", ["$greater", "C1", "A1"]], "=>", ["smallest", "A", "B", "C"]]],

["forall", ["A", "B", "C", "A1", "B1", "C1"], [[["Area", "A", "A1"], "&", ["Area", "B", "B1"], "&", ["Area", "C", "C1"], "&", ["$greater", "A1", "B1"], "&", ["$greater", "C1", "B1"]], "=>", ["smallest", "B", "A", "C"]]],

["forall", ["A", "B", "C", "A1", "B1", "C1"], [[["Area", "A", "A1"], "&", ["Area", "B", "B1"], "&", ["Area", "C", "C1"], "&", ["$greater", "A1", "C1"], "&", ["$greater", "B1", "C1"]], "=>", ["smallest", "C", "A", "B"]]],

["~smallest", "Pedassaar 14", "Rammu saar 12", "K\u00f5rksaar 13"]
```

**Response:**

```json
{
  "result": "proof found",

  "answers": [
    {
      "proof": [
        [
          1,
          ["in", "frm_90"],
          [
            ["smallest", "?:X", "?:Y", "?:Z"],
            ["-$greater", "?:U", "?:V"],
            ["-$greater", "?:W", "?:V"],
            ["-Area", "?:Z", "?:W"],
            ["-Area", "?:Y", "?:U"],
            ["-Area", "?:X", "?:V"]
          ]
        ],
        [2, ["in", "frm_81"], [["Area", "Kõrksaar 13", 0.91]]],
        [
          3,
          ["mp", [1, 3], 2],
          [
            ["smallest", "?:X", "?:Y", "Kõrksaar 13"],
            ["-$greater", 0.91, "?:Z"],
            ["-$greater", "?:U", "?:Z"],
            ["-Area", "?:Y", "?:U"],
            ["-Area", "?:X", "?:Z"]
          ]
        ],
        [4, ["in", "frm_78"], [["Area", "Rammu saar 12", 1.12]]],
        [
          5,
          ["mp", [3, 3], 4],
          [
            ["smallest", "?:X", "Rammu saar 12", "Kõrksaar 13"],
            ["-$greater", 1.12, "?:Y"],
            ["-$greater", 0.91, "?:Y"],
            ["-Area", "?:X", "?:Y"]
          ]
        ],
        [6, ["in", "frm_83"], [["Area", "Pedassaar 14", 0.9]]],
        [
          7,
          ["in", "frm_91"],
          [["-smallest", "Pedassaar 14", "Rammu saar 12", "Kõrksaar 13"]]
        ],
        [8, ["mp", [5, 3], 6, 7], false]
      ]
    }
  ]
}
```

**In words**

Kolmest saarest kõige väiksem on **Pedassaar**.

# ✅ Conclusion

This homework demonstrates a significant gap between natural language model reasoning and formal logic-based inference. Claude Sonnet 4, although fluent and seemingly confident, produced incorrect answers in both test cases:

- It overestimated Nigula’s size compared to Tõhela.
- It underestimated Pedassaar’s smallness compared to Kõrksaar and Rammu saar.

⚠️ Takeaway:
Large language models can be misleading in knowledge-based queries without grounding in structured logic or verified data. Gathering the data manually and formatting with LLM and verifying with logic based reasoning tools (logitools) gives better result
