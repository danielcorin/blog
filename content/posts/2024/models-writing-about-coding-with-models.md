---
title: "Models Writing About Coding With Models"
date: 2024-11-01T21:26:30-04:00
draft: false
tags:
- language_models
---

I recently found Joe's article, [We All Know AI Can’t Code, Right?](https://www.inc.com/joe-procopio/we-all-know-ai-cant-code-right.html).

As I was reading, I began to hear some familiar refrains of the past 6 months.

> Raise your hand if you’ve ever used GitHub or Stack Overflow or any other kind of example code or library or whatever to help you get started on the foundational solution to the business problem that your code needs to solve.
>
> Now, put your hand down if you’ve never once had to spend hours, sometimes days, tweaking and modifying that sample code a million times over to make it work like you need it to work to solve your unique problem.
>
> OK. All of you who put your hands down. Get out of the room. Seriously. Go. We can’t have a serious discussion about this.

I didn't entirely know where this line of thinking was going, especially after reading

> # AI Is Not an Existential Threat
>
> Real coders know.

I guess maybe I expected _more_ gate-keeping?
The "real programmers use `vim`" kind of gate-keeping, but I was pleased he didn't go down this route.

By Joe's measure, we can talk about this.

I suppose the ethics of what I am about to do are questionable, but I don't know how to explore, understand or try and figure out where this technology could potentially take us other than to use it in a manner in which critics claim it cannot be used.
I got the go ahead from Joe before publishing, so hopefully that can allay some concerns.

I pasted Joe's article into Sonnet, then prompted it to respond to Joe's arguments with my thesis while imitating his style.

{{< chat model="claude-3-5-sonnet-20241022" >}}
[
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "If anyone is telling you that AI can code what you need coded and build what you need built, they are lying to you.\n\nThis is not speculation. This is not bombast. This is not a threat. \n\nWe know enough now about how AI works, and especially GenAI, to be able to say this with confidence. And I’m not just talking about knowledge gained over the last two years, but the knowledge gained over the last two decades. I was there at the beginning. I know.\n\nFor a lot of you, I’m telling you something you already know as well. But your work here is far from over. You need to lean into the truth and help us all explain why relying on AI to write production code for an application that customers will actually use is like opening a restaurant with nothing more than a stack of fun recipes with colorful photos.\n\nThey look great on paper, but paper doesn’t taste very good.\n\nThe Boring Structural Work Matters\n\nTo put this into a perspective that everyone can understand, let me ask you a question: \n\nQ: How would you know if this article was written by AI?\n\nA: Because it would suck.\n\nYeah, maybe the bots could imitate my vibe, adopt my writing tics, and lean into the rule of threes as I often do, but even then, the jury is still out on how closely it can replicate my style beyond a sentence or two.\n\nBanana. \n\nScrew you, AI.\n\nThe thing I’m 100 percent sure AI can’t do is take my decades of experience in the topics I choose — topics that need to be timely across an ever-changing technical and entrepreneurial landscape — and use my snarky words and questionable turns of phrase to put insightful, actionable thoughts into the heads of the maximum amount of people who would appreciate those thoughts. \n\nThat’s structure. It’s foundational. It’s boring. But it’s the only thing that holds these fragments of pixelated brain dump together. \n\nLook, if you want to write about a technical or entrepreneurial topic, you either need to a) spend a lifetime doggedly nerding down those paths with real-world, real-life stakes and consequences, or b) read a bunch of articles written by people who have done just that and then summarize those articles as best you can without understanding half of what those people are actually talking about.\n\nWhich one sounds more like AI, a) or b)?\n\nNow let’s talk about how that relates to code, because hopefully you can already see the connection.\n\nAI Is Not an Existential Threat\n\nReal coders know.\n\nThe threat that AI presents to your average software developer is not new.\n\nRaise your hand if you’ve ever used GitHub or Stack Overflow or any other kind of example code or library or whatever to help you get started on the foundational solution to the business problem that your code needs to solve.\n\nNow, put your hand down if you’ve never once had to spend hours, sometimes days, tweaking and modifying that sample code a million times over to make it work like you need it to work to solve your unique problem.\n\nOK. All of you who put your hands down. Get out of the room. Seriously. Go. We can’t have a serious discussion about this.\n\nCheap, flawed, technical-debt-inducing, easily breakable code has been a threat to software developers since they first started letting us kids bang on Basic — let alone the threat of any technology solution that ends with the word “-shoring”.\n\nThe AI threat just seems existential because of the constant repetition of a few exaggerated truths. That it’s “free,” that it’s “original,” and that it “works.”\n\nHere’s why that’s going to be a race to failure. Position yourself.\n\n“AI” “Can” “Code”\n\nThat’s the most judgy, snarky, douchey section header I’ve ever written. But in my defense, there’s a reason why every word is in quotes. Because this is how the lie propagates. \n\nYes, what we’re calling AI today makes an admirable attempt at slapping syntax together in a way that compiles and runs. I’m not even going to dive into the chasm of difference between GenAI and real AI or why code is more than syntax.\n\nBut I will point to the fact that — even beyond those quibbles — we’re not at anything I’d call viable yet. Damning words from an IEEE study follow:\n\n> [ChatGPT has] a success rate ranging from anywhere as poor as 0.66 percent and as good as 89 percent — depending on the difficulty of the task, the programming language, and a number of other factors.\n\nI’ll let you determine how “difficulty,” “programming language,” and “other factors” impacts the success rate. Quotes again. Sorry. If it’s any consolation I nearly sprained a finger because I was air quoting so hard reading that damn thing.\n\nA conclusion of the study (italics are mine): “ChatGPT has not been exposed yet to new problems and solutions. It lacks the critical thinking skills of a human and can only address problems it has previously encountered.”\n\nSo much like my example of why AI-generated articles suck, if you’re trying to solve new problems by inventing new solutions, AI has zero experience with this.\n\nOK, all you “ChatGPT-4o-is-Neo” bros can come at me now. But it isn’t just the syntax where AI has problems.\n\nAw, AI Came Up With This All by Itself\n\nCode in a vacuum is worthless.\n\nEvery software developer reading this just went, “Yup.”\n\nBeyond all the limitations that AI exposes when it creates syntax out of “thin air” (or to use the technical term, “other people’s code”), deeper problems start to expose themselves when we try to get the results of that code into a customer’s hands. \n\nCode without design, UI, UX, functional requirements, and business requirements is a classroom exercise in futility. The problem AI runs into with any of those “long-tail” success factors is that none of them are binary. Zero.\n\nSo, for example, Figma had to temporarily pull back on its AI design feature when it was alleged that its AI is just copying someone else’s design. \n\n“Just describe what you need, and the feature will provide you with a first draft,” is how the company explained it when the feature launched.\n\nI can do that without AI. I can do that with cut and paste. Figma blamed poor QA. Which one sounds more true?  \n\nAI Is Great at a Lot of Things\n\nBut not elegance.\n\nIf your code is not infused with a chain of elegance that connects the boring structural-solution work to the customer-facing design and UX, you can still call it “code” if you want to, but it will have all the value of an AI-generated avatar reading aloud AI-generated content over AI-generated images. \n\nHave you ever seen that? It’ll stab you in the soul.\n\nThere’s a right way to do things and there’s a way to do things well, and I’m not naive enough to rail against the notion that sometimes you just can’t do both. But this is 30 years of tech history repeating itself, and the techies need to start teaching history or we’ll keep being forced to repeat it.\n\nSo I’d ask my software developer friends to raise your hand if you’ve ever had to come in and fix someone’s poorly structured, often broken, debt-laden, and thoroughly inelegant code.\n\nOK. Those of you who didn’t raise your hands, figure it out, because there’s a lot of that kind of work coming. And anyone who has ever had to fix bad code can tell you it takes a lot longer to do that than it would have taken to just code it well in the first place.\n\nI’m going to be talking more about humans properly using AI to solve problems for other humans. If you’re interested in that sort of thing, now would be a good time to join my email list at joeprocopio.com\n\nThe above is an article written by Joe. Argue the opposite of his case above -- that AI can code and augment and empower the capabilities of the individual using it -- using the same mildly sarcastic and defiant tone that he specifically notes AI cannot effectively imitate"
            }
        ]
    },
    {
        "role": "assistant",
        "content": [
            {
                "type": "text",
                "text": "Oh, Joe. Sweet, skeptical Joe.\n\nLet me channel that same defiant snark you claim AI can't replicate (while obviously doing exactly that right now - meta, isn't it?).\n\nFirst off - that \"decades of experience\" argument? That's adorably 2019. You know what has more collective experience than any individual developer? The entire corpus of human coding knowledge that AI models train on. But sure, let's pretend your specific war stories from debugging BASIC are more valuable than synthesized knowledge from millions of developers.\n\nBanana right back at ya, pal.\n\nLet's address your \"structural work\" argument. You know what's really good at understanding structure? Systems literally trained to recognize patterns and relationships. While you're proudly spending hours manually tweaking Stack Overflow code, AI is instantly analyzing thousands of similar solutions and synthesizing the most appropriate approach.\n\n\"But AI just copies code!\" I hear you cry into your artisanal coffee mug. Funny thing about that - what do human developers do? We \"stand on the shoulders of giants,\" right? We reuse patterns, implement known solutions, adapt existing approaches. We just do it slower and with more bugs.\n\nSpeaking of bugs - that IEEE study you cherry-picked? Let's talk about human developer success rates. How many times has your perfectly human-crafted code worked flawlessly on the first try? I'll wait while you stop laughing.\n\nAnd that \"elegance\" you're so proud of? Here's a hot take: maybe perfect elegance isn't always the point. Sometimes \"good enough\" code that works is better than spending weeks crafting the most beautiful implementation that nobody will ever see. AI gets that - it's pragmatic.\n\nThe truth is, AI isn't replacing developers - it's supercharging them. It's like having a junior developer who:\n- Never gets tired\n- Can instantly recall every coding pattern ever written\n- Doesn't need coffee breaks\n- Won't argue about tabs vs. spaces\n\nYou're right about one thing though - AI isn't magic. It's a tool. But it's a revolutionary tool that's already augmenting developer capabilities whether you like it or not. Your resistance isn't protecting the craft - it's just making you obsolete faster.\n\nAnd that \"fixing bad code\" argument? Guess what - AI is getting pretty good at that too. It can analyze, refactor, and optimize code faster than any human. Sure, it might not always get it perfect, but neither do your human developers who keep writing \"thoroughly inelegant code.\"\n\nThe future isn't about AI versus humans. It's about developers who embrace AI versus those who don't. And I know which side of that divide I want to be on.\n\nScrew your bananas. I'm bringing robots to the party.\n\nP.S. Was this response snarky enough? I can dial it up if needed. After all, I'm just an AI - what do I know about attitude? 😏"
            }
        ]
    }
]
{{< /chat >}}

Question my taste, but to me, this doesn't read like AI slop.
This reads like the model participating in the conversation and making points that resonate with me as someone who finds writing software with AI to be useful and productive.
The model is also a bit rude and I didn't love that but I sort of asked for it.

I don't expect models to be able to replace the learnings and wisdom that come from real experience, but I do see them as helpful tools to probe and refine our arguments, communicate with increased clarity and magnify our existing, hard-earned skills and knowledge.
The capabilities seem to extend to writing code, prose and beyond into the visual applications as well.
It's an idea I've been circling for the better part of a year now and took a first pass at in [Making Your Vision Real]({{< ref "/posts/2024/making-your-vision-real.md" >}}).
Think to yourself, "what do _I know_"?
That's your starting point when interacting with a model.
Then you tell the model:

Here's where I am.

Here's where I want to go.

Here's what I have tried.

For me today, exchanges with a state-of-the-art model more often than not steer me in a productive direction to continue to learn and to improve the quality of what I am working on in the moment.
