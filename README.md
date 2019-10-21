# postscrapper

--------------
postscrapper ,a slack bot keeps you up-to-date about all the facebook pages you care about 




## Usage

##### /post
- from any slack channel just type `/post [pageid]`.Top 10 recent post would be displayed of that page.
- eg : /post nytimes<br />
      here,<br />
      pageid=nytimes<br />
     
      

## Integrate it with your team


1. Go to your channel
2. Goto `https://[team_name].slack.com/apps/manage/custom-integrations	`.
3. Click on **Add** next to **Slash Commands**.


   1. For usage as shown in above gif image
   
       - Command: `/post`
       - URL: `https://postscrapper.herokuapp.com/post`
       - method: `POST`
       - For the **Autocomplete help text**, check to show the command in autocomplete list.
       - Description: `give recent 10 post of the page.`
       - Usage Hint: `[pageid]`.
 

## Contributing
- Please use the [issue tracker](https://github.com/ankit96/postscrapper/issues) to report any bugs or file feature requests.

## LICENCE
- Credits: Inspired by [@minimaxir's](https://github.com/minimaxir/facebook-page-post-scraper) facebook-page-post-scraper.
- [MIT LICENSE](https://github.com/ankit96/postscrapper/blob/master/LICENSE) (c) Ankit Sagwekar
