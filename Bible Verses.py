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
   {
      "reference": "1 Thessalonians 5:18",
      "text": "Give thanks in all circumstances; for this is God’s will for you in Christ Jesus.",
      "description": "Gratitude is an act of faith — thank God even through the ordinary and hard moments."
    },
    {
      "reference": "Psalm 100:4",
      "text": "Enter his gates with thanksgiving and his courts with praise; give thanks to him and praise his name.",
      "description": "Approach God with a thankful heart and celebrate His goodness."
    },
    {
      "reference": "Colossians 3:15",
      "text": "Let the peace of Christ rule in your hearts, since as members of one body you were called to peace. And be thankful.",
      "description": "Peace and gratitude go hand-in-hand in the life of faith."
    },
    {
      "reference": "James 1:17",
      "text": "Every good and perfect gift is from above, coming down from the Father of the heavenly lights, who does not change like shifting shadows.",
      "description": "Every good and perfect gift comes from God, who never changes. He is constant and faithful, the source of all goodness in our lives."
    }
  ],
  "broken":[
    {
      "reference": "Psalm 34:18",
      "text": "The LORD is close to the brokenhearted and saves those who are crushed in spirit.",
      "description": "When your heart is shattered, God draws near to bring comfort and healing."
    },
    {
      "reference": "Psalm 147:3",
      "text": "He heals the brokenhearted and binds up their wounds.",
      "description": "God is a gentle healer — you can bring your wounds to Him."
    },
    {
      "reference": "Matthew 11:28",
      "text": "Come to me, all who labor and are heavy laden, and I will give you rest.",
      "description": "Jesus invites the hurting to come and receive rest."
    },
    {
      "reference": "Romans 8:18",
      "text": "I consider that our present sufferings are not worth comparing with the glory that will be revealed in us.",
      "description": "The sufferings we face now are nothing compared to the glory God will reveal in us. It’s a reminder to stay hopeful, knowing something far greater is coming."
    }
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