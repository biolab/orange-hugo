+++
author="Janez Demšar"
date= '2019-09-28'
draft= true
title="On Expected Vomiting Time"
type="blog"
thumbImage = "/blog_img/2019-09-28-vomiting-pumpkin.jpg"
frontPageImage = "/blog_img/2019-09-28-vomiting-pumpkin.jpg"
categories=["model performance", "confusion matrix"]
shortExcerpt = "Computing meaningful performance scores of models should be creative"
longExcerpt = "A report of an interesting ending of a lecture about setting probability thresholds for predictive models"
+++

We just finished a lecture and a student came with a question. The lecture was, in short, about how predictive models compute probabilities, and to make decisions we must find a threshold that will minimize the cost, maximize the profit, strike a good balance between sensitivity and specificity, or increase the general human well-being in some other way. So this student came with a question about something I didn't explain well, and she gave me one last chance.

I had some data that looked like this.

| ID | predicted probabilities | аctual class |
| -: | ----------------------: | ------------ | 
|  1 | 0.984                   | p            |
|  2 | 0.907                   | p            |
|  3 | 0.881                   | n            |
|  4 | 0.865                   | n            |
|  5 | 0.815                   | p            |
|  6 | 0.741                   | p            |
|  7 | 0.735                   | p            |
|  8 | 0.635                   | n            |
|  9 | 0.582                   | n            |
| 10 | 0.480                   | p            |
| 11 | 0.413                   | n            |
| 12 | 0.317                   | n            |
| 13 | 0.287                   | n            |
| 14 | 0.225                   | n            |
| 15 | 0.216                   | p            |
| 16 | 0.183                   | n            |


The data is made up, so I had to make up its meaning to form an example. In the rush of a moment, I succumbed to classics: "*For each of those 16 people you predicted the probability for being sick. Whom are you going to give the cure?*" Her answer was in line with the best manners of modern medical practice (who cares about bacteria becoming resistant to antibiotics?): "*To all!*" I didn't expect this, but anyway planned to continue with emphasizing that this medicine is not harmless: "*People who take this medicine will vomit for one week.*" She turned by 180 degrees: "*Oh, no. To nobody!*" I didn't expect this either. I spend two weeks a year teaching in Moscow, and gosh I love these students! Her decision led nicely to my next condition: "*But if a person is indeed sick and you don't give him the drug, he'll vomit for four weeks.*"

Decision making becomes much more interesting when both, yes and no, have consequences.

So, to restate:
- if you give the medicine to anybody, sick or healthy, he vomits for a week. 
- If you don't give the cure to a sick person, he vomits for four weeks -- and you can no longer help him after he starts.


### Optimal threshold

To solve the problem, we had to compute the *expected vomiting time*. This being a fairly new medical term, we need to define it. For instance, what would be the *expected vomiting time* for a person who is sick with a probability of 0.865? If we have 1000 people with such probability of being sick, 865 will vomit (for four weeks) and 135 won't.
- If we don't give this 1000 people the medicine, 865 will vomit for 4 weeks, hence the total vomiting time will be 4 x 865 = 3460 weeks, or 3.460 weeks per person, where the average includes those who are not vomiting. This is of course the same as if we just multiplied 4 x 0.865, without multiplying and then dividing by 1000.
- If we give these 1000 people the medicine, all 1000 will vomit for a week, thus totalling 1000 weeks of vomiting or, obviously, 1 week per person.

The latter option is better. Administering the medicine will reduce the *expected vomiting time* (per person) from 3.460 weeks to 1 week. Well done.

What about people with 0.216 probability of being sick? Expected vomiting time of such persons is 4 x 0.216 = 0.864, which is less than a week. No drug for them. (The poor bloke with the 0.216 probability is actually sick. But we don't know this yet. S..t happens. I mean, vomit happens.)

Obviously, the optimal threshold here is 0.250, which gives the expected vomiting time of 1 week, with or without the drug. We should administer the drug to all except the last three people in the list.

We could have computed this threshold even before having the model. It is a property of the disease and the drug, not the model.

For an extra task, compute the expected vomiting time with this threshold. Note that you can't assume that 1/4 of untreated people will vomit for 4 weeks: some of them may also have just 12 % or 3 % chance of being sick.


### Optimal threshold for the model

We have so far used just probabilities and ignored the information whether somebody is sick (p) or not (n), which is given in the third column. We also assumed that predicted probabilities were correct because we had nothing else to go by.

Now let us take the true status into account and see how this allows for deciding better thresholds. We can now compute the actual vomiting times for using the model at particular thresholds.

If we indeed used the threshold of 0.25 and administered the drug to the first 13 people, we'd have 13 people vomiting for 1 week, and the poor guy #15 suffering for 4, which gives us (well, them) the total vomiting time of 13 + 4 = 17 weeks. (We will just compute total vomiting times now; no need to going "per person", since we'd always just divide by 16.)

If we instead used a treshold of 0.2, 15 people would vomit for one week and nobody for four. This reduces total vomiting time to 15 weeks.

(The actual story we developed with the student was slightly different, but roughly at this point, a student who was doing something else and has just started listening to our debate about expected and total vomiting times, interrupted us with: "*Who are all these people and why are they vomiting?*" We had to explain her that nobody is vomiting and that we just have a *sick* sense for examples.)

But there's an even better threshold. If we give the drug only to people whose probability is at least 0.48, 10 people will vomit for one week and the poor guy #15 for four weeks, giving us a total of 14 weeks of vomiting. Or 14 / 16 = 0,875 weeks per person.

We shouldn't go any higher. Every sick person whom we don't give a drug needs to be counterbalanced by at least three healthy people being freed from a one-week ordeal, and there are not enough healthy persons left above 0.48.

In this way, we simulated what would happen if we used this model on this know population of people. So if we use it in practice and our goal is to reduce the total (or average) vomiting time, we know to administer the drug to everybody with p >= 0.48.

Why the discrepancy? Why isn't the threshold that we computed above, 0.250, also the optimal threshold? 0.250 would be the optimal threshold if predicted probabilities were true probabilities. Model's may be badly calibrated. While there exist methods for fixing their calibration (though not with so little data), we here took a more direct approach and computed the treshold for probabilities as predicted by our model.

### Pedagogical Moral

The nice thing about the story is that we didn't care about classification accuracy. Oh, yes, after fixing the threshold to 0.48, we can compute it (it's 11/16 -- just cound the p's above and n's below the treshold). We also see that the probability of administering a drug to a healthy person (and making him needlessly hug the toilet for seven days) is 40 %, because in our sample, we had 4 such cases out of 10 whom we gave the drug. We call such poor victims *false positives*, and 40 % is the *false discovery rate*. The miserables whom we don't give the drug though we should, are *false negatives*. The *false omission rate* (being sick if you're not given a drug) is 1/6. The probability of not being given the drug if you're sick (*miss rate* or *false negative rate*) is 1/7. I'm of course just copying this from Wikipedia. Nobody knows the entire list of names.

As a lecturer, I believe that emphasizing this list of names too much may do more harm than good. I usually show them the list just to say that all these things have names, but then try to compute something meaningful and not fancy-named. Try forcing them to learn the list and then give them a task like above. They'll likely spend the entire exam guessing whether you want them to compute *specificity* or *critical success index* -- instead of simply computing the *expected vomiting time*. Which is not even on Wikipedia.

Yet.