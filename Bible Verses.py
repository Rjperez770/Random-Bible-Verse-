import random
from textwrap import fill

#The bible verses that are grouped by feelings
verse_blank = {
  "anxious": [
    {
      "reference": "Philippians 4:6-7",
      "text": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
      "description": "When worry runs high, prayer and thanksgiving invite God's peace into your heart"
    },
    {
      "reference": "John 14:27",
      "text": "Peace I leave with you; my peace I give to you. Not as the world gives do I give to you. Let not your hearts be troubled, neither let them be afraid.",
      "description": "Peace I leave with you; my peace I give to you. Not as the world gives do I give to you. Let not your hearts be troubled, neither let them be afraid."
    },
    {
      "reference": "1 Peter 5:7",
      "text": "Cast all your anxiety on him because he cares for you.",
      "description": "You aren't meant to carry anxiety alone give it to God, who cares deeply for you."
    },
    {
      "reference": "Matthew 6:34",
      "text": "Therefore do not worry about tomorrow, for tomorrow will worry about itself.",
      "description": "Focus on today; God is faithful about the future one step at a time."
    }
  ],
  "lonely": [
    {
      "reference": "Psalm 23:4",
      "text": "Even though I walk through the darkest valley, I will fear no evil, for you are with me.",
      "description": "In your loneliest valleys, God walks alongside you — you are not alone."
    },
    {
      "reference": "Deuteronomy 31:6",
      "text": "Be strong and courageous. Do not be afraid or terrified... for the LORD your God goes with you; he will never leave you nor forsake you.",
      "description": "God's promise: He goes with you and will not abandon you."
    },
    {
      "reference": "Hebrews 13:5",
      "text": "Never will I leave you; never will I forsake you.",
      "description": "A short, powerful reminder of God's constant presence."
    },
    {
      "reference": "Joshua 1:9",
      "text": "Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go",
      "description": "Have I not commanded you? Be strong and courageous. Do not be frightened, and do not be dismayed, for the Lord your God is with you wherever you go"
    }
  ],
  "grateful":[

  ],
  "broken":[

  ],
  "tempted":[

  ],
  "hopeless":[

  ],
  "joyful":[

  ],
  "fearful":[

  ]
}