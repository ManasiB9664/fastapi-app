import requests

# URL of the APIs (make sure to adjust the ports if needed)
CLASSIFY_API_URL = "http://127.0.0.1:8000/classify-text/"
SUMMARIZE_API_URL = "http://127.0.0.1:8001/summarize/"

# Function to classify the text into categories using the classification API
def classify_text(text):
    # Send the request to the classify-text API
    response = requests.post(CLASSIFY_API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json()  # Return the categorized clauses
    else:
        print("Error classifying text:", response.status_code)
        return None

# Function to summarize text using the summarization API
def summarize_text(text):
    # Send the request to the summarize API
    response = requests.post(SUMMARIZE_API_URL, json={"text": text})
    if response.status_code == 200:
        return response.json().get("summary", "")  # Return the summary
    else:
        print("Error summarizing text:", response.status_code)
        return None

# Main function to classify and summarize the text
def classify_and_summarize(text):
    # Step 1: Classify the text into categories
    classified_data = classify_text(text)
    if not classified_data:
        print("No classified data found.")
        return

    # Step 2: Summarize each category of classified text
    summaries = {}
    for category, clauses in classified_data.items():
        category_summary = []
        for clause in clauses:
            summary = summarize_text(clause)
            if summary:
                category_summary.append(summary)
        summaries[category] = category_summary

    return summaries

# Example usage
if __name__ == "__main__":
    # Example text (replace with your actual input text)
    example_text = """
1. The Instagram Service
We agree to provide you with the Instagram Service. The Service includes all of the Instagram products, features, applications, services, technologies, and software that we provide to advance Instagram's mission: To bring you closer to the people and things you love. The Service is made up of the following aspects:
Offering personalized opportunities to create, connect, communicate, discover and share. People are different. So we offer you different types of accounts and features to help you create, share, grow your presence, and communicate with people on and off Instagram. We also want to strengthen your relationships through shared experiences that you actually care about. So we build systems that try to understand who and what you and others care about, and use that information to help you create, find, join and share in experiences that matter to you. Part of that is highlighting content, features, offers and accounts that you might be interested in, and offering ways for you to experience Instagram, based on things that you and others do on and off Instagram.
Fostering a positive, inclusive, and safe environment.
We develop and use tools and offer resources to our community members that help to make their experiences positive and inclusive, including when we think they might need help. We also have teams and systems that work to combat abuse and violations of our Terms and policies, as well as harmful and deceptive behavior. We use all the information we have-including your information-to try to keep our platform secure. We also may share information about misuse or harmful content with other Meta Companies or law enforcement. Learn more in the Privacy Policy.
Developing and using technologies that help us consistently serve our growing community.
Organizing and analyzing information for our growing community is central to our Service. A big part of our Service is creating and using cutting-edge technologies that help us personalize, protect, and improve our Service on an incredibly large scale for a broad global community. Technologies like artificial intelligence and machine learning give us the power to apply complex processes across our Service. Automated technologies also help us ensure the functionality and integrity of our Service. Learn more in the Privacy Policy.
Providing consistent and seamless experiences across other Meta Company Products.
Instagram is part of the Meta Companies, which share technology, systems, insights, and information-including the information we have about you (learn more in the Privacy Policy) in order to provide services that are better, safer, and more secure. We also provide ways to interact across the Meta Company Products that you use, and designed systems to achieve a seamless and consistent experience across the Meta Company Products depending on your choices.
Ensuring access to our Service.
To operate our global Service, we must store and transfer data across our systems around the world, including outside of your country of residence. The use of this global infrastructure is necessary and essential to provide our Service. This infrastructure may be owned or operated by Meta Platforms, Inc., Meta Platforms Ireland Limited, or their affiliates. For more information about how we transfer, store or process your information, please review our Privacy Policy.
Connecting you with brands, products, and services in ways you care about.
We use data from Instagram and other Meta Company Products, as well as from third-party partners, to show you ads, offers, and other sponsored content that we believe will be meaningful to you. And we try to make that content as relevant as all your other experiences on Instagram.
Research and innovation.
We use the information we have to study our Service and collaborate with others on research to make our Service better and contribute to the well-being of our community.

2. How Our Service Is Funded
Instead of paying to use Instagram, by using the Service covered by these Terms, you acknowledge that we can show you ads that businesses and organizations pay us to promote on and off the Meta Company Products. We use your personal data, such as information about your activity and interests, to show you ads that are more relevant to you.
We show you relevant and useful ads without telling advertisers who you are. We don’t sell your personal data. We allow advertisers to tell us things like their business goal and the kind of audience they want to see their ads. We then show their ad to people who might be interested.
We also provide advertisers with reports about the performance of their ads to help them understand how people are interacting with their content on and off Instagram. For example, we provide general demographic and interest information to advertisers to help them better understand their audience. We don’t share information that directly identifies you (information such as your name or email address that by itself can be used to contact you or identifies who you are) unless you give us specific permission. Learn more about how Instagram ads work here.
You may see branded content on Instagram posted by account holders who promote products or services based on a commercial relationship with the business partner mentioned in their content. You can learn more about this here.

3. The Privacy Policy
Providing our Service requires collecting and using your information. The Privacy Policy explains how we collect, use, and share information across the Meta Products. It also explains the many ways you can control your information, including in the Instagram Privacy and Security Settings. You must agree to the Privacy Policy to use Instagram.

4. Your Commitments
In return for our commitment to provide the Service, we require you to make the below commitments to us.
4.1 Who Can Use Instagram. We want our Service to be as open and inclusive as possible, but we also want it to be safe, secure, and in accordance with the law. So, we need you to commit to a few restrictions in order to be part of the Instagram community.
You must be at least 13 years old or the minimum legal age in your country to use Instagram.
You must not be prohibited from receiving any aspect of our Service under applicable laws or engaging in payments related Services if you are on an applicable denied party listing.
We must not have previously disabled your account for violation of law or any of our policies.
You must not be a convicted sex offender.
4.2 How You Can't Use Instagram. Providing a safe and open Service for a broad community requires that we all do our part.
You can't impersonate others or provide inaccurate information.
You don't have to disclose your identity on Instagram, but you must provide us with accurate and up to date information (including registration information), which may include providing personal data. Also, you may not impersonate someone or something you aren't, and you can't create an account for someone else unless you have their express permission.
You can't do anything unlawful, misleading, or fraudulent or for an illegal or unauthorized purpose.
You can't violate (or help or encourage others to violate) these Terms or our policies, including in particular the Community Standards, Meta Platform Terms and Developer Policies, and Music Guidelines.
If you post branded content, you must comply with our Branded Content Policies, which require you to use our branded content tool. Learn how to report conduct or content in our Help Center.
You can't do anything to interfere with or impair the intended operation of the Service.
This includes misusing any reporting, dispute, or appeals channel, such as by making fraudulent or groundless reports or appeals.
You can't attempt to create accounts or access or collect information in unauthorized ways.
This includes creating accounts or accessing or collecting information in an automated way without our express permission, regardless of whether such automated access or collection is undertaken while logged-in to an Instagram account.
You can’t sell, license, or purchase any account or data obtained from us or our Service, regardless of whether such data was obtained while logged-in to an Instagram account.
This includes attempts to buy, sell, or transfer any aspect of your account (including your username); solicit, collect, or use login credentials or badges of other users; or request or collect Instagram usernames, passwords, or misappropriate access tokens.
You can't post someone else’s private or confidential information without permission or do anything that violates someone else's rights, including intellectual property rights (e.g., copyright infringement, trademark infringement, counterfeit, or pirated goods).
You may use someone else's works under exceptions or limitations to copyright and related rights under applicable law. You represent you own or have obtained all necessary rights to the content you post or share. Learn more, including how to report content that you think infringes your intellectual property rights, here.
You can’t modify, translate, create derivative works of, or reverse engineer our products or their components.
You can't use a domain name or URL in your username without our prior written consent.
You can't do, or attempt to do, anything to circumvent, by-pass, or override any technological measures that control or limit access to the Service or data.
4.3 Permissions You Give to Us. As part of our agreement, you also give us permissions that we need to provide the Service.
We do not claim ownership of your content, but you grant us a license to use it.
Nothing is changing about your rights in your content. We do not claim ownership of your content that you post on or through the Service and you are free to share your content with anyone else, wherever you want. However, we need certain legal permissions from you (known as a “license”) to provide the Service. When you share, post, or upload content that is covered by intellectual property rights (like photos or videos) on or in connection with our Service, you hereby grant to us a non-exclusive, royalty-free, transferable, sub-licensable, worldwide license to host, use, distribute, modify, run, copy, publicly perform or display, translate, and create derivative works of your content (consistent with your privacy and application settings). This license will end when your content is deleted from our systems. You can delete content individually or all at once by deleting your account. To learn more about how we use information, and how to control or delete your content, review the Privacy Policy and visit the Instagram Help Center.
Permission to use your username, profile picture, and information about your relationships and actions with accounts, ads, and sponsored content.
You give us permission to show your username, profile picture, and information about your actions (such as likes) or relationships (such as follows) next to or in connection with accounts, ads, offers, and other sponsored content that you follow or engage with that are displayed on Meta Products, without any compensation to you. For example, we may show that you liked a sponsored post created by a brand that has paid us to display its ads on Instagram. As with actions on other content and follows of other accounts, actions on sponsored content and follows of sponsored accounts can be seen only by people who have permission to see that content or follow. We will also respect your ad settings. You can learn more here about your ad settings.
You agree that we can download and install updates to the Service on your device.

5. Additional Rights We Retain
If you select a username or similar identifier for your account, we may change it if we believe it is appropriate or necessary (for example, if it infringes someone's intellectual property or impersonates another user).
If you use content covered by intellectual property rights that we have and make available in our Service (for example, images, designs, videos, or sounds we provide that you add to content you create or share), we retain all rights to our content (but not yours).
You can only use our intellectual property and trademarks or similar marks as expressly permitted by our Brand Guidelines or with our prior written permission.
You must obtain written permission from us or under an open source license to modify, create derivative works of, decompile, or otherwise attempt to extract source code from us.

6. Content Removal and Disabling or Terminating Your Account
We can remove any content or information you share on the Service if we believe that it violates these Terms of Use, our policies (including our Community Standards), or we are permitted or required to do so by law. We work with independent fact-checkers in many jurisdictions to combat misinformation. When content has been rated by fact-checkers, we may add a notice to provide additional context. You can find more information about fact-checking here. We can refuse to provide or stop providing all or part of the Service to you (including terminating or disabling your access to the Meta Products and Meta Company Products) immediately to protect our community or services, or if you create risk or legal exposure for us, violate these Terms of Use or our policies (including our Community Standards), if you repeatedly infringe other people's intellectual property rights, or where we are permitted or required to do so by law. We can also terminate or change the Service, remove or block content or information shared on our Service, or stop providing all or part of the Service if we determine that doing so is reasonably necessary to avoid or mitigate adverse legal or regulatory impacts on us. If you believe your account has been terminated in error, or you want to disable or permanently delete your account, consult our Help Center. When you request to delete content or your account, the deletion process will automatically begin no more than 30 days after your request. It may take up to 90 days to delete content after the deletion process begins. While the deletion process for such content is being undertaken, the content is no longer visible to other users, but remains subject to these Terms of Use and our Privacy Policy. After the content is deleted, it may take us up to another 90 days to remove it from backups and disaster recovery systems.
Content will not be deleted within 90 days of the account deletion or content deletion process beginning in the following situations:
where your content has been used by others in accordance with this license and they have not deleted it (in which case this license will continue to apply until that content is deleted); or
where deletion within 90 days is not possible due to technical limitations of our systems, in which case, we will complete the deletion as soon as technically feasible; or
where deletion would restrict our ability to:
investigate or identify illegal activity or violations of our terms and policies (for example, to identify or investigate misuse of our products or systems);
protect the safety and security of our products, systems, and users;
comply with a legal obligation, such as the preservation of evidence; or
comply with a request of a judicial or administrative authority, law enforcement or a government agency;
in which case, the content will be retained for no longer than is necessary for the purposes for which it has been retained (the exact duration will vary on a case-by-case basis).
If you delete or we disable your account, and you stop accessing or using Instagram, or if this contract is otherwise terminated, then these Terms shall terminate as an agreement between you and us, but this section, the section above called “Your Commitments,” and the section below called "Our Agreement and What Happens if We Disagree" will still apply even after your account is terminated, disabled, or deleted, or this contract is otherwise terminated.

7. Our Agreement and What Happens if We Disagree
7.1 Our Agreement.
Your use of music on the Service is also subject to our Music Guidelines, and your use of our API is subject to our Meta Platform Terms and Developer Policies. If you use certain other features or related services, additional terms will be made available and will also become a part of our agreement. For example, if you use payment features, you will be asked to agree to the Community Payment Terms. If you use Avatars, then the Avatar Terms also apply. If you use our AI products and features, the Meta AI Terms also apply. If any of those terms conflict with this agreement, those other terms will govern.
If any aspect of this agreement is unenforceable, the rest will remain in effect.
Any amendment or waiver to our agreement must be in writing and signed by us. If we fail to enforce any aspect of this agreement, it will not be a waiver.
We reserve all rights not expressly granted to you.
7.2 Who Has Rights Under this Agreement.
This agreement does not give rights to any third parties.
You cannot transfer your rights or obligations under this agreement without our consent.
Our rights and obligations can be assigned to others. For example, this could occur if our ownership changes (as in a merger, acquisition, or sale of assets) or by law.

7.3 Who Is Responsible if Something Happens.
Our Service is provided "as is," and we can't guarantee it will be safe and secure or will work perfectly all the time. TO THE EXTENT PERMITTED BY LAW, WE ALSO DISCLAIM ALL WARRANTIES, WHETHER EXPRESS OR IMPLIED, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT.
We also don’t control what people and others do or say, and we aren’t responsible for their (or your) actions or conduct (whether online or offline) or content (including unlawful or objectionable content). We also aren’t responsible for services and features offered by other people or companies, even if you access them through our Service.
Our responsibility for anything that happens on the Service (also called "liability") is limited as much as the law will allow. If there is an issue with our Service, we can't know what all the possible impacts might be. You agree that we won't be responsible ("liable") for any lost profits, revenues, information, or data, or consequential, special, indirect, exemplary, punitive, or incidental damages arising out of or related to these Terms, even if we know they are possible. This includes when we delete your content, information, or account.
7.4 How We Will Handle Disputes.
If you are a consumer, the laws of the country in which you reside will apply to any claim, cause of action, or dispute you have against us that arises out of or relates to these Terms ("claim"), and you may resolve your claim in any competent court in that country that has jurisdiction over the claim. In all other cases, you agree that the claim must be resolved exclusively in the U.S. District Court for the Northern District of California or a state court located in San Mateo County, that you submit to the personal jurisdiction of either of these courts for the purpose of litigating any such claim, and that the laws of the State of California will govern these Terms and any claim, without regard to conflict of law provisions. Without prejudice to the foregoing, you agree that, in its sole discretion, Meta Platforms Inc. may also bring any claim we have against you related to efforts to abuse, interfere, or engage with our products in unauthorized ways in the country in which you reside that has jurisdiction over the claim.
7.5 Unsolicited Material.
We always appreciate feedback or other suggestions, but may use them without any restrictions or obligation to compensate you for them, and are under no obligation to keep them confidential.

8. Updating These Terms
We may change our Service and policies, and we may need to make changes to these Terms so that they accurately reflect our Service and policies. Unless otherwise required by law, we will notify you (for example, through our Service) before we make changes to these Terms and give you an opportunity to review them before they go into effect. Then, if you continue to access or use the Service, you will be bound by the updated Terms. If you do not agree to any updated Terms or wish to terminate your agreement to this contract, you can do so by deleting your account here and no longer accessing or using any part of the Instagram Service.
    """

    # Call the classify_and_summarize function
    summaries = classify_and_summarize(example_text)

    # Print out the summaries
    if summaries:
        for category, summary_list in summaries.items():
            print(f"\n{category}:")
            for summary in summary_list:
                print(summary)
                print()
            print()
