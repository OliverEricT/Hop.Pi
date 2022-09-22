DROP TABLE IF EXISTS HopPi.Style;

/*####################################

    Debug Block

    SELECT * FROM HopPI.Style

####################################*/

CREATE TABLE HopPi.Style(
   StyleId int PRIMARY KEY AUTO_INCREMENT
  ,Name varchar(100)
  ,Description varchar(4000)
);

INSERT INTO HopPi.Style(
     Name
    ,Description
)
VALUES
     ('Standard American Beer','This category describes everyday American beers that have a wide public appeal. Containing both ales and lagers, the beers of this category are not typically complex, and have smooth, accessible flavors. The ales tend to have lager-like qualities, or are designed to appeal to mass-market lager drinkers as crossover beers. Mass-market beers with a more international appeal or origin are described in the International Lager category.')
    ,('International Lager','International lagers are the premium, industrial, mass-market lagers produced in most countries in the world. Whether developed from American or European styles, they all tend to have a fairly uniform character and are heavily marketed. Loosely derived from original Pilsner-type lagers, with colored variations having additional malt flavors while retaining a broad appeal. In many countries, the styles will be referred to by their local country names. The use of the term “international” doesn’t mean that any beers are actually labeled as such, but is more of a categorization of similar beers produced worldwide.')
    ,('Czech Lager','Czech lagers are generally divided by gravity class (draft, lager, special) and color (pale, amber, dark). The Czech names for these categories are světlé (pale), polotmavé (amber), and tmavé (dark). The gravity classes are výčepní (draft, 7–10 °P), ležák (lager, 11–12 °P), and speciální (special, 13 °P+). Pivo is of course the Czech word for beer. The division into gravity classes is similar to the German groupings of schankbier, vollbier, and starkbier, although at different gravity ranges. Czech beers within the classes are often simply referenced by their gravity. There are often variations within the gravity-color groupings, particularly within the speciální class. The style guidelines combine some of these classes, while other beers in the Czech market are not described (such as the strong Czech Porter). This is not to imply that the categories below are the full coverage of Czech beers, simply a way of grouping some of the more commonly found types for judging purposes. Czech lagers in general are differentiated from German and other Western lagers in that German lagers are almost always fully attenuated, while Czech lagers can have a slight amount of unfermented extract remaining in the finished beer. This helps provide a slightly higher finishing gravity (and thus slightly lower apparent attenuation), slightly fuller body and mouthfeel, and a richer, slightly more complex flavor profile in equivalent color and strength beers. German lagers tend to have a cleaner fermentation profile, while Czech lagers are often fermented cooler (7–10 °C) and for a longer time, and can have a light, barely noticeable (near threshold) amount of diacetyl that often is perceived more as a rounded body than overtly in aroma and flavor [significant buttery diacetyl is a flaw]. Czech lager yeast strains are not always as clean and attenuative as German strains, which helps achieve the higher finishing gravity (along with the mashing methods and cooler fermentation). Czech lagers are traditionally made with decoction mashes (often double decoction), even with modern malts, while most modern German lagers are made with infusion or step infusion mashes. These differences characterize the richness, mouthfeel, and flavor profile that distinguishes Czech lagers.')
    ,('Pale Malty European Lager','This style category contains pale German lagers of vollbier to starkbier strength that emphasize the flavor of Pilsner malt in the balance while remaining well-attenuated.')
    ,('Pale Bitter European Beer','This category describes German-origin beers that are pale and have an even to bitter balance with a mild to moderately strong hoppy character featuring traditional German hops. They are generally bottom-fermented or are lagered to provide a smooth profile, and are well-attenuated as are most German beers.')
    ,('Amber Malty European Beer','This category groups amber-colored, German-origin, bottom-fermented lagerbiers that have a malty balance and are vollbier to starkbier in strength.')
    ,('Amber Bitter European Beer','This category groups amber-colored, evenly balanced to bitter balanced beers of German or Austrian origin.')
    ,('Dark European Lager','This category contains German vollbier lagers darker than amber-brown color.')
    ,('Strong European Beer','This category contains more strongly flavored and higher alcohol lagers from Germany and the Baltic region. Most are dark, but some pale versions are known.')
    ,('German Wheat Beer','This category contains vollbier- and starkbier-strength German wheat beers without sourness, in light and dark colors.')
    ,('British Bitter','The family of British bitters grew out of English pale ales as a draught product after the late 1800s. The use of crystal malts in bitters became more widespread after WWI. Traditionally served very fresh under no pressure (gravity or hand pump only) at cellar temperatures (i.e., “real ale”). Most bottled or kegged versions of UK-produced bitters are often higher-alcohol and more highly carbonated versions of cask products produced for export, and have a different character and balance than their draught counterparts in Britain (often being sweeter and less hoppy than the cask versions). These guidelines reflect the “real ale” version of the style, not the export formulations of commercial products.  Several regional variations of bitter exist, ranging from darker, sweeter versions served with nearly no head to brighter, hoppier, paler versions with large foam stands, and everything in between. Judges should not over-emphasize the caramel component of these styles. Exported bitters can be oxidized, which increases caramel-like flavors (as well as more negative flavors). Do not assume that oxidation-derived flavors are traditional or required for the style. ')
    ,('Pale Commonwealth Beer','This category contains pale, moderately-strong, hop-forward, bitter ales from countries within the former British Empire.')
    ,('Brown British Beer','While Dark Mild, Brown Ale, and English Porter may have long and storied histories, these guidelines describe the modern versions. They are grouped together for judging purposes only since they often have similar flavors and balance, not because of any implied common ancestry. The similar characteristics are low to moderate strength, dark color, generally malty balance, and British ancestry. These styles have no historic relationship to each other; especially, none of these styles evolved into any of the others, or was ever a component of another. The category name was never used historically to describe this grouping of beers; it is our name for the judging category. “Brown Beer” was a distinct and important historical product, and is not related to this category name.')
    ,('Scottish Ale','There are really only three traditional beer styles broadly available today in Scotland: the 70/- Scottish Heavy, the 80/- Scottish Export, and the Strong Scotch Ale (Wee Heavy, Style 17C). The 60/- Scottish Light is rare and often cask-only, but it does seem to be having a bit of a renaissance currently. All these styles took modern form after World War II, regardless of prior use of the same names. Currently, the 60/- is similar to a dark mild, the 70/- is similar to an ordinary bitter, and the 80/- similar to a best or strong bitter. The Scottish beers have a different balance and flavor profile, but fill a similar market position as those English beers. The Light, Heavy, and Export beers have similar flavor profiles, and are often produced through the parti-gyling process. As gravity increases, so does the character of the beer. Traditional ingredients were dextrinous pale ale malt, corn, dark brewing sugars, and brewers caramel for coloring. Modern (post-WWII) recipes often add small amounts of dark malt and lower percentages of crystal malt, along with other ingredients like amber malt and wheat. Scottish brewers traditionally used single infusion mashes, often with underlet mashes and multiple sparges. In general, these Scottish beers are weaker, sweeter, darker, lower in attenuation, and less highly hopped compared to equivalent modern English beers. They are produced using slightly cooler fermentation temperatures than their counterparts. Many of these differences have been exaggerated in popular lore; they are noticeable, but not huge, yet enough to affect the balance of the beer, and to perhaps indicate a national flavor preference. The balance remains malty and somewhat sweet due to higher finishing gravity, lower alcohol, and lower hopping rates. Many of these divergences from English beer took place between the late 1800s and the mid-1900s. Production methods championed by homebrewers, such as kettle caramelization or grists heavy in a variety of crystal malts, are not commonly used in traditional products but can approximate those flavors when traditional ingredients aren’t available. The use of peat-smoked malt is not only completely inauthentic, it produces a dirty, phenolic flavor inappropriate in any of these styles. Smoked versions (using any type smoke) should be entered in 32A Classic Style Smoked Beer. The use of ‘shilling’ (/-) designations is a Scottish curiosity. Originally it referred to the price of beer in hogshead casks, which in no way could be constant over time. Shillings aren’t even used as a currency now in Scotland. But the name stuck as a shorthand for a type of beer, even if the original meaning stopped being the real price during WWI. About all it means now is that larger numbers mean stronger beers, at least within the same brewery. Between the world wars, some breweries used the price per pint rather than shillings (e.g., Maclay 6d for 60/-, 7d for 70/-, 8d for 80/-). Confusingly, during this time 90/- pale ale was a low-gravity bottled beer. Curious, indeed.')
    ,('Irish Beer','The traditional beers of Ireland contained in this category are amber to dark, top-fermented beers of moderate to slightly strong strength, and are often widely misunderstood due to differences in export versions, or overly focusing on the specific attributes of beer produced by high-volume, well-known breweries. Each of the styles in this grouping has a wider range than is commonly believed.')
    ,('Dark British Beer','This category contains average to strong, bitter to sweet, modern British and Irish stouts that originated in England even if some are now more widely associated with Ireland. In this case, “British” means the broader British Isles not Great Britain.')
    ,('Strong British Ale','This category contains stronger, non-roasty ales of the British Isles.  Covers the style space above bitters, milds, and brown ales while excluding porters and stouts.')
    ,('Pale American Ale','This category contains modern American ales of average strength and light color that are moderately malty to moderately bitter.')
    ,('Amber and Brown American Beer','This category contains modern American amber and brown top-fermented ales and warm-fermented lagers of standard strength that can be balanced to bitter.')
    ,('American Porter and Stout','These beers all evolved from their English namesakes to be wholly transformed by American craft brewers. Generally, these styles are bigger, stronger, more roast-forward, and more hop-centric than their traditional Anglo cousins. These styles are grouped together due to a similar shared history and flavor profile.')
    ,('IPA','The IPA category is for modern American IPAs and their derivatives. This does not imply that English IPAs aren’t proper IPAs or that there isn’t a relationship between them. This is simply a method of grouping similar styles for competition purposes. English IPAs are grouped with other English-derived beers, and the stronger Double IPA is grouped with stronger American beers. The term “IPA” is intentionally not spelled out as “India Pale Ale” since none of these beers historically went to India, and many aren’t pale. However, the term IPA has come to be a balance-defined style in modern craft beer.')
    ,('Strong American Ale','This category includes modern American strong ales with a varying balance of malt and hops. The category is defined mostly by higher alcohol strength and a lack of roast.')
    ,('European Sour Ale','This category contains the traditional sour beer styles of Europe that are still produced, many (but not all) with a wheat component. Most have low bitterness, with the sourness of the beer providing the balance that hop bitterness would otherwise contribute. Some are sweetened or flavored, whether at the brewery or upon consumption.')
    ,('Belgian Ale','This category contains the maltier to balanced, more highly flavored Belgian and French ales.')
    ,('Strong Belgian Ale','')
    ,('Monastic Ale','')
    ,('Historical Beer','')
    ,('American Wild Ale','')
    ,('Fruit Beer','')
    ,('Spiced Beer','')
    ,('Alternative Fermentables Beer','')
    ,('Smoked Beer','')
    ,('Wood Beer','')
    ,('Specialty Beer','');