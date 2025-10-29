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
    {
      "reference": "1 Corinthians 10:13",
      "text": "No temptation has overtaken you except what is common to mankind. And God is faithful; he will not let you be tempted beyond what you can bear.",
      "description": "Temptation is common, but God provides a way through it — you are not defeated."
    },
    {
      "reference": "James 4:7",
      "text": "Submit yourselves therefore to God. Resist the devil, and he will flee from you.",
      "description": "Resisting temptation starts with submitting to God — it's an active, powerful choice."
    },
    {
      "reference": "Matthew 26:41",
      "text": "Watch and pray so that you will not fall into temptation. The spirit is willing, but the flesh is weak.",
      "description": "Prayer and awareness help you stand firm when your resolve wanes."
    },
    {
      "reference":"Hebrews 2:18",
      "text": "For because he himself has suffered when tempted, he is able to aid those who are tempted.",
      "description": "Because Jesus suffered and was tempted, He understands our struggles and is able to help us when we face temptation."
    }
  ],
  "hopeless":[
    {
      "reference": "Romans 15:13",
      "text": "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit.",
      "description": "God is the source of true hope — trusting Him replenishes joy and peace."
    },
    {
      "reference": "Jeremiah 29:11",
      "text": "For I know the plans I have for you... plans to give you hope and a future.",
      "description": "Even when things look bleak, God has a good plan for your future."
    },
    {
      "reference": "Psalm 42:11",
      "text": "Why, my soul, are you downcast? Put your hope in God...",
      "description": "Talk to your soul and re-anchor hope in God — He is steady."
    },
    {
      "reference": "Philippians 4:13",
      "text": "I can do all this through him who gives me strength.",
      "description": "With Christ’s strength, we can endure and accomplish anything. His power gives us the ability to overcome challenges and keep moving forward."
    }
  ],
  "joyful":[
    {
      "reference": "Philippians 4:4",
      "text": "Rejoice in the Lord always. I will say it again: Rejoice!",
      "description": "Celebrate — joy in the Lord is a repeated, daily command and gift."
    },
    {
      "reference": "Psalm 16:11",
      "text": "You make known to me the path of life; in your presence there is fullness of joy.",
      "description": "True, overflowing joy is found in God's presence."
    },
    {
      "reference": "Nehemiah 8:10",
      "text": "The joy of the LORD is your strength.",
      "description": "Let God's joy power you through the day."
    },
    {
      "reference": "1 Thessalonians 5:16-18",
      "text": "Rejoice always, pray continually, give thanks in all circumstances; for this is God's will for you in Christ Jesus.",
      "description": "We’re called to rejoice always, pray continually, and give thanks in every situation. This is God’s will for us, helping us stay grounded in faith no matter what happens."
    }
  ],
  "fearful":[
    {
      "reference": "Isaiah 41:10",
      "text": "So do not fear, for I am with you; do not be dismayed, for I am your God.",
      "description": "God's presence removes the power of fear — He strengthens and helps you."
    },
    {
      "reference": "Psalm 56:3",
      "text": "When I am afraid, I put my trust in you.",
      "description": "Fear can be met with the simple act of trusting God."
    },
    {
      "reference": "2 Timothy 1:7",
      "text": "God gave us a spirit not of fear but of power and love and self-control.",
      "description": "You have God's Spirit within you — it empowers you beyond fear."
    },
    {
      "reference": "Philippians 4:6-7",
      "text": "Do not be anxious about anything, but in every situation, by prayer and petition, with thanksgiving, present your requests to God. And the peace of God, which transcends all understanding, will guard your hearts and your minds in Christ Jesus.",
      "description": "We are encouraged not to be anxious but to bring our requests to God in prayer with thanksgiving. In return, His peace, beyond all understanding, will guard our hearts and minds."
    }
  ]
}

# Synonyms for flexibility
Synonms_Map = {
  "worried":"anxious",
  "stressed":"anxious",
  "alone":"lonely",
  "thankful":"grateful",
  "sad":"broken",
  "hurt":"broken",
  "temptation":"tempted",
  "down":"hopeless",
  "depressed":"hopeless",
  "happy":"joyful",
  "afraid":"fearful",
  "scared":"fearful"
}