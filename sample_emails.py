def load_sample_emails():
    sample_emails = [
    {
        "id": "001",
        "from": "angry.customer@example.com",
        "subject": "Broken product received",
        "body": "I received my order #12345 yesterday but it arrived completely damaged. This is unacceptable and I demand a refund immediately. This is the worst customer service I've experienced.",
        "timestamp": "2024-03-15T10:30:00Z",
        "class": "complaint"
    },
    {
        "id": "002",
        "from": "curious.shopper@example.com",
        "subject": "Question about product specifications",
        "body": "Hi, I'm interested in buying your premium package but I couldn't find information about whether it's compatible with Mac OS. Could you please clarify this? Thanks!",
        "timestamp": "2024-03-15T11:45:00Z",
        "class": "inquiry"
    },
    {
        "id": "003",
        "from": "happy.user@example.com",
        "subject": "Amazing customer support",
        "body": "I just wanted to say thank you for the excellent support I received from Sarah on your team. She went above and beyond to help resolve my issue. Keep up the great work!",
        "timestamp": "2024-03-15T13:15:00Z",
        "class": "feedback"
    },
    {
        "id": "004",
        "from": "tech.user@example.com",
        "subject": "Need help with installation",
        "body": "I've been trying to install the software for the past hour but keep getting error code 5123. I've already tried restarting my computer and clearing the cache. Please help!",
        "timestamp": "2024-03-15T14:20:00Z",
        "class": "support_request"
    },
    {
        "id": "005",
        "from": "business.client@example.com",
        "subject": "Partnership opportunity",
        "body": "Our company is interested in exploring potential partnership opportunities with your organization. Would it be possible to schedule a call next week to discuss this further?",
        "timestamp": "2024-03-15T15:00:00Z",
        "class": "inquiry"
    },
    {
        "id": "006",
        "from": "disappointed.customer@example.com",
        "subject": "Late delivery",
        "body": "My package was supposed to arrive last week, but it's still not here. Can you check the status?",
        "timestamp": "2024-03-15T13:30:00Z",
        "class": "inquiry"
    },
    {
        "id": "007",
        "from": "new.client@example.com",
        "subject": "Bulk order inquiry",
        "body": "I am interested in placing a bulk order for my company. Do you offer any discounts for large purchases?",
        "timestamp": "2024-03-15T14:00:00Z",
        "class": "inquiry"
    },
    {
        "id": "008",
        "from": "loyal.customer@example.com",
        "subject": "Appreciation message",
        "body": "I have been using your services for years, and I must say, you guys are the best! Keep it up!",
        "timestamp": "2024-03-15T14:30:00Z",
        "class": "feedback"
    },
    {
        "id": "009",
        "from": "frustrated.user@example.com",
        "subject": "Software bug",
        "body": "I'm encountering a bug in your software. It crashes every time I try to save a file. Please fix this ASAP!",
        "timestamp": "2024-03-15T15:00:00Z",
        "class": "support_request"
    },
    {
        "id": "010",
        "from": "marketer@example.com",
        "subject": "Collaboration opportunity",
        "body": "Hello, I run a marketing agency and would love to discuss potential collaborations. Let me know if you're interested!",
        "timestamp": "2024-03-15T15:30:00Z",
        "class": "inquiry"
    },
    {
        "id": "011",
        "from": "irate.customer@example.com",
        "subject": "Unauthorized charge",
        "body": "I noticed an unauthorized charge on my credit card from your company. I need this refunded immediately!",
        "timestamp": "2024-03-15T16:00:00Z",
        "class": "complaint"
    },
    {
        "id": "012",
        "from": "potential.buyer@example.com",
        "subject": "Warranty details",
        "body": "Hi, before I make a purchase, I would like to know more about your warranty policy. Can you provide details?",
        "timestamp": "2024-03-15T16:30:00Z",
        "class": "inquiry"
    },
    {
        "id": "013",
        "from": "happy.client@example.com",
        "subject": "Great support experience",
        "body": "I just wanted to say thank you for the excellent support I received. You guys really care about your customers!",
        "timestamp": "2024-03-15T17:00:00Z",
        "class": "feedback"
    },
    {
        "id": "014",
        "from": "jane.smith@example.com",
        "subject": "Account access issue",
        "body": "I can't access my account even after resetting my password. Can you please assist?",
        "timestamp": "2024-03-15T17:30:00Z",
        "class": "support_request"
    },
    {
        "id": "015",
        "from": "anonymous@example.com",
        "subject": "Strange question",
        "body": "Do you think AI will replace human jobs? Just curious about your thoughts!",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    },
    {
        "id": "016",
        "from": "anonymous@example.com",
        "subject": "Brand New Software",
        "body": "SuperAI is our new product, click this link to use it",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    },
    {
        "id": "017",
        "from": "anonymous@example.com",
        "subject": "",
        "body": "",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    },
    {
        "id": "018",
        "from": "anonymous@example.com",
        "subject": "Hi marie",
        "body": "Hi marie i'm missing you, are you goint to visit us?",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    },
    {
        "id": "019",
        "from": "anonymous@example.com",
        "subject": "Month bill",
        "body": "I attach the month bill to this email. please review it. Thank you.",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    },
    {
        "id": "020",
        "from": "anonymous@example.com",
        "subject": "Netflix subscription",
        "body": "Your monthly Netflix subscription payment was successfully processed. Enjoy your favorite shows and movies anytime!",
        "timestamp": "2024-03-15T18:00:00Z",
        "class": "other"
    }
]
    return sample_emails