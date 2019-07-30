+++
author="Dr. Sven Bingert & Steffen Rörtgen"
date= '2019-07-02'
draft= false
title="Data Science Made Easy: How To Identify Hate Comments with AI"
type="blog"
thumbImage = "/blog_img/2019/twitter-police-workshop-picture.jpeg"
frontPageImage = "/blog_img/2019/twitter-police-workshop-picture.jpeg"
categories=["education", "text mining", "workshop"]
shortExcerpt = "How to teach text mining and data science to the 9th grade students in 60 minutes?"

longExcerpt = "How to teach text mining and data science to the 9th grade students in 60 minutes? With Orange and the analysis of hate speech on social media, of course!"
+++

The [IdeenExpo](https://www.ideenexpo.de/) is a biennial participatory event for children, adolescents and young adults taking place in Hanover, Germany. Companies, research organizations, schools and universities participate to show young people the possibilities of the modern working world and gain their interest in technologies and natural sciences. As a part of one of the biggest research-computing-centers in North Germany the [GWDG](https://www.gwdg.de/home) (Gesellschaft für wissenschaftliche Datenverarbeitung mbh Göttingen) took a part in that event to present the possibilities of Data Science and how its methods can be used in different areas.

Related: {{< link_new url="blog/2018/09/11/text-workshops-in-ljubljana/" name="Text Workshops in Ljubljana">}}

Our goal was to give the 9th grade students a 60-minute hands-on introduction to some possible real-life use cases. As we were working with Orange3 now for some time, we decided to use it in our workshop, because it has the great benefit of being able to do data analysis without the need to write code, which wouldn't have worked in a 60 minute workshop.

{{% figure src="/blog_img/2019/twitter-police-workshop-picture.jpeg" width="80%" caption="" %}}
\

We started with some introductory talks and discussions about the presence of Big Data in our daily life to get some insights into the existing knowledge of the students. A quick question about who is active in social media made it clear that everyone in that workshop has one or more accounts on social media platforms. Next we asked about hate comments on social media and everyone was aware about that topic as well.

After displaying some hate comments and discussing about how we as humans identify them, we split the group in two parts. One group had then to write hate comments and insults, whereas the other group wrote neutral comments concerning a certain topic we decided on.

We then collected that comments in a GoogleSheets Table, labeled them and every student opened Orange3 on his or her laptop. The students were asked to explain in their own words how they would train an "AI" to learn to distinguish between hate and neutral comments and we showed them how this can be translated in an Orange workflow. This way the students already learned that we have to do some preprocessing to filter out uninformative words for example.

{{% figure src="/blog_img/2019/data-science-made-easy-workflow.png" caption="Final workflow." %}}
\

With just the tweets we made up in our session we gained a precision value of 0.66 in the first session and after we appended the tweets from the second group, we already gained a value of 0.76. Afterwards the students were asked to made up 4 other tweets the model was not trained on and used the Predictions widget to see how well our model performed. Well, we just got the results we would have thought of, if we would have had to classify them on our own!

Orange3 made it possible to develop a model for detecting hate comments in just 60 minutes with students, who had no programming skills. Thanks to the Orange Team!
