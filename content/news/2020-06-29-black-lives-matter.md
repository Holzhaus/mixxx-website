title: "#BlackLivesMatter: Taking a Stand with Terminology and Recruitment"
authors: Mixxx Team, April M. Crehan
tags: black lives matter, diversity, community, outreachy
date: 2020-06-29 15:00:00

Alongside the protesters in the US and around the world, the Mixxx team unequivocally condemns police brutality.
The systemic racism that burdens people of color every day is the responsibility of white people around the world to address.
Mixxx' core development team feels it necessary not to remain silent on this issue, for ["silence in the face of injustice is complicity with the oppressor."](https://www.theguardian.com/news/2000/sep/14/guardianobituaries)

Going beyond the hashtag, we have been discussing concrete actions we can take as a community and today we announce two efforts: first, to **[eliminate master/slave terminology](https://www.washingtonpost.com/opinions/2020/06/12/tech-industry-has-an-ugly-master-slave-problem/) from our code base** and second, to **recruit paid interns from underrepresented communities** to join our contributor base.

## Terminology Changes

Major projects like [Python](https://www.vice.com/en_us/article/8x7akv/masterslave-terminology-was-removed-from-python-programming-language), [Go](https://www.reddit.com/r/golang/comments/gy9ylr/go_has_removed_all_uses_of_blacklistwhitelist_and/fte1zk0/), and now [Github](https://www.cnet.com/news/microsofts-github-is-removing-coding-terms-like-master-and-slave/) have all worked to eliminate the use of the [problematic](https://blog.carbonfive.com/problematic-terminology-in-open-source/) terms, "master" and "slave," and today Mixxx joins them.
The issue of nomenclature and terminology in software is one example of how deeply embedded white privilege is around the globe and we hope changing these terms is one small step towards a more inclusive and diverse coding community.

Although we eliminated the use of the word "slave" back in [2016](https://github.com/mixxxdj/mixxx/commit/e59916caf72a256bb28b1722759a629c5cc9cf81), "master" still appears in a number of places.
We have a "master" code branch, a "Master Sync" feature, an "EngineMaster" object, and more.
We are working to migrate our code away from these words, even in many cases where the particular meaning of "master" was never explicitly associated with a problematic context.

It’s important to note that there will be some cases where the word will remain.
Many DJ controllers have buttons marked "master" on them, and we need to refer to those buttons by name.
There are also the audio engineering concepts of a "master tape" or "audio mastering", so there may be areas of our documentation or code that would be less understandable if we tried to use synonyms.
But in situations where "master" is used in code, we commit to changing the language we use in the next major release, Mixxx version 2.4.

But changing language is not enough.

## Building A More Diverse Community

As an entirely online community that allows anyone to participate with a pseudonym, we don't know the exact demographic makeup of our contributors.
Our impression, however, is that the Mixxx contributor base is largely white, male, and either from the US or Western Europe.
This is especially disappointing given that people of color played a foundational role in [creating DJing as an art form in the US and elsewhere](https://www.dukeupress.edu/Love-Saves-the-Day/).
Technology companies have a tacit (and sometimes explicit) expectation that prospective employees "prove themselves" by contributing to open source projects. Companies also often value referrals, which increase the likelihood that new hires will be similar to previous hires, thus perpetuating homogeneity.

We want to break this cycle and ensure that the door to our open source network is open to everyone.
It is our goal to make both the Mixxx community and the software we make as inclusive, accessible and welcoming as possible.
As such, it is our responsibility to actively seek out and promote the participation of groups who are underrepresented in our community.

Research shows that blind admission and hiring tends to result in less diverse outcomes.
To that end, we plan to participate in the [Outreachy](https://www.outreachy.org/) program and have a paid internship position by December 2020, the next available cycle.
Outreachy’s stated goal is to provide "internships to work in open source and free software, for women (both cis and trans), trans men, and genderqueer people" and "residents and nationals of the United States of any gender who are Black/African American, Hispanic/Latin@, Native American/American Indian, Alaska Native, Native Hawaiian, or Pacific Islander."
They encourage "anyone who faces under-representation, systemic bias, or discrimination in the technology industry of their country" to apply.

Our goal is that this Outreachy intern will be one of an increasing number of valued contributors from more diverse backgrounds that will help us be a healthier, more sustainable open source project.
Provided that we're able to raise sufficient funds, we commit to participate in Outreachy for at least 2 cycles.  At that time we'll evaluate our progress and decide if we'll continue our participation or focus on other ways to support BIPOC.

One Outreachy intern will cost Mixxx $6,500 to sponsor.
To fund our two cycles of interns, we'll need $13,000.
As a project that is entirely community-driven, we are looking to you, our collaborators and users, to secure the funding for this effort. There is no company behind Mixxx.
All Mixxx developers are volunteers that work on Mixxx in their free time.
We [have never and will never charge for Mixxx](/news/2020-05-22-you-dont-need-to-pay-for-mixxx/), so this is a chance for you to contribute money that will go directly to a person working on the project.

We are currently working out the details of our fundraiser and we hope to have it launched in the next couple weeks.

We're aware that replacing some terms and participating in Outreachy might seem insignificant in light of the discrimination and violence that people of color and Black people in particular face every day.
As a project that depends on donations and volunteer work, we invite all our collaborators and users to discuss further community action on [Zulip](https://mixxx.zulipchat.com) as we continue to stand against racism and discrimination.
Keep protesting!
