1.What are some product design questions you ask in Facebook Full stack SWE interviews?

Product design questions are not that different from System design questions, the only difference being the problem statement will be more product-oriented than a low-level infra system. For example - if a system design question is - "Design the backend of a push notification layer for a messaging service", the product design question would look like - "Design FB Messenger". Product Design questions are generally more vague and the interviewer expects you to breakdown the given Problem -> Product -> Features -> API -> DB. At each level they would expect you to prioritize key problems, key features and key solutions to focus on. And finally, they look for similar things as system design in your answer i.e. talk about Scalability, Redundancy, Availability, Backup/Restoration but in context of overall product-level features. For e.g. talk about scalability if the given product can scale to a large number of users, focus more availability if the given problem is say a Financial product where reliability is very critical. Similarly, you should also talk about how you'd deal with Spam/Abuse, Security/hackers, etc depending on the problem. Hope you got the gist!

Here are some sample questions - "Design an Email server", "Design a collaborative rich document editor (like Google Docs)", "Design Twitter", "Design Whatsapp Pay".
2.What are the key pointers you're looking out for when you evaluate this interview? Also, if you've interviewed at the E5/6 level, please talk about what specifically you look for in an E6 that you wouldn't find in an E5

3 things -
1. Problem breakdown and coverage - whether the candidate has successfully able to figure out the key problem areas to focus on, key features and how to implement them. More importantly the features you picked should cover most of the use-cases and critical user-journeys of the product. For e.g. don't forget talking about client-side push notifications when designing a chat service.

2. Maturity/depth in the answer - When deep-diving on any feature, talk more thoroughly about what stack/db/language you'd use and why. Even write sample pseudo-code if needed to explain a complex algorithm instead of hand-waving stuff. Whether you can find all corner-cases and different things that can go wrong in your own design and whether you have preemptively handled those cases. Is your solution future-proof?

3. User champion - This is very key and is actually one of the differentiators between E5 and E6. Are you able to talk about the user experience of your product and solution? Can you see whether the solution you're designing will lead to a good user journey or not? Instead of thinking too much from system/infra, can you also think from the user-side and incorporate changes in your design to delight the user?

Between E5 and E6, the key pointers are the same just that the bar is much higher. For E6, expectation is that you're a strong IC with amazing design chops and you would excel in all those key pointers while needing minimum intervention from the interviewer. For E5 expectation is slightly less but still on the high side. "User champion" is one angle that most E5 don't talk that much about but E6s are able to incorporate very early in their design.

1.What are some product design questions you ask in Facebook Full stack SWE interviews?

Hi - here are a few examples. We have a question bank of ~100 design questions, so you're unlikely to get one of these specifically, but it'll give you a sense for the types of questions we might ask.

1. Design a URL shortening service, from the ground up. Which systems do we need? How do we scale it to some arbitrarily large (billions) of txns per day? How do we generate the URLs? What does a system diagram look like for both the read and write flows? How are spam and malicious links handled? How might we be able to track and display traffic stats to users?

2. Design news feed. This question is very broad, and can be approached from either a product API or system diagram perspective. You'll get questions like: how do we handle incremental fetches for infinite scrolling? What type of caching can we handle? Load balancing? You might also get some questions about chronological vs. ranked feeds, and the pros/cons of each, how to empirically optimize a ranked feed.

3. Build a translation engine. Suppose it's 2006 and Facebook is taking off, but we have hardcoded English strings all throughout the codebase, and want to internationalize the site. How do we abstract away the language into a central translation service? What would the storage layer look like (i.e. DB tables)? How do we build an interface for translators to receive the raw strings from engineers and convert to each language? How do we add new languages? What if we wanted to crowdsource translations to the public -- what are the pros/cons of that, and how would we approach?
2.What are the key pointers you're looking out for when you evaluate this interview? Also, if you've interviewed at the E5/6 level, please talk about what specifically you look for in an E6 that you wouldn't find in an E5

Interview performance on this interview is less indicative of leveling than other ones. In fact, performance at anything above E5 is expected to be the same, whereas we expect higher performance in other interviews. But that being said, we do want you do well in this interview or it'll raise some red flags in your candidacy.

Here's some quick detail on the type of signal we're looking for:

a) For you to lead the conversation. These interviews go best when you do 80+% of the talking. This shows you're able to fully ingest a problem and lead from concept to solution.
b) Identify the options, make reasonable assumptions, and be decisive.
c) Walk up and down the stack. Part of this interview looks for you to able to give a high level summary and broad strategy, and also to get into the technical details of how to build it. It should be technical and *not* high level or hand-wavey.

Key areas for you to hit:

- Identify options, articulate pros/cons, and make a decision.
- Scalability, modularity, support.
- Aim to define a system or product with enough detail that a team of junior engineers sitting in on the interview could walk out and start building.

Best of luck!
