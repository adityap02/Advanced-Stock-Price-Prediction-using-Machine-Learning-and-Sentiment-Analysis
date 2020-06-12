from textblob import TextBlob
from textblob import Word
from textblob.classifiers import NaiveBayesClassifier
from textblob.classifiers import PositiveNaiveBayesClassifier

relevant = [
'It will also unleash a torrent of demand for $Tsla shares. The SP will likely move very fast because Tesla is so well positioned for global growth',
'This the time to Buy, buy buy. What would you do if Apple or Tesla is putting their products on sale. Won’t you borrow and hustle to go and buy',
' Tesla shares rise on report Volkswagen CEO is interested in stake',
'zachary kirkhorn sells 150 shares of tesla inc $tsla stock',
'Due to fall in share price of RBL Bank, HDFC Ltd investment in RBL Bank equity shares suffers a loss of Rs 184 crore for which loss provision is to be made FVTPL investment by HDFC Ltd ',
'some of stocks i feel give good returns after listening to you and doing my research are  Icici bank, inox, Sbi,HDFC,Relaxo,SBI life',
'Looking at the volume parameters in some banking stocks like bajaj finance and hdfc bank , sharp recovery on the cards. Anytime',
'Sensex falls 850 points as HDFC twins bleed 184 stocks hit 52-week lows on BSE',
'Don’t hurry in buying stocks for long term look at hdfc and Bajaj finance Fiis are selling it like anything ',
' The Indian stockmarket continues trading in the red with Sensex down 3.76% and #Nifty down 3.48%',
'Todays volatille market and ative closing will create few but not great opportunities to buy when you already entered at better price. I will buy again Infosys, reliance and hdfc bnk, and TCS only if they will come back to 550, 900, 780 and 1700 or below respectively',
'Banking stocks witnessed massive selloff led by ICICI Bank HDFC Bank, which contributed 75% to the Nifty Bank’s fall Brokerages say that the disruption of the domestic and global economies due to coronavirus will have a meaningful impact on banks’ loan-book growth',
'HDFC Bank, ITC among 10 stocks that could benefit from stimulus package',
'netflix is now worth more than exxon as the coronavirus lockdown sends shares soaring',
'positive sentiment on social media for $tsla. significant activity  for tesla. ',
'tesla shares up over 5% after beating analysts estimates for q1  get all the latest $tsla related news here :  ',
'tesla shares dip after initial surge on upbeat deliveries   ',
' my shares went crashing down 37 in an hour uhhhh',
'tesla shares up over 5% after beating analysts estimates for q1  via  ',
'tesla stock continues june rebound as shares rise again  ',
'tesla shares soared after its first-quarter delivery numbers impressed investors',
'tesla shares soared after its first-quarter delivery numbers impressed investors',
'tesla shares soar 20% on stronger-than-expected deliveries amid coronavirus outbreak ',
'ford not gonna rule much longer.',
' my tesla shares went down 37 in an hour uhhhh',
'glad i spent today buying and buying tsla. only wish i could have afforded more than 3.2 shares. with you all the way  ',
'tesla sold half my shares thinking they would be ative numbers like all analysts were saying.',
' my tesla shares went +37 in an hour ',
' my tesla shares went plus 37 in an hour ',
'tesla shares soar as it beats delivery forecasts despite factory shutdowns ',
'tesla shares up over 5% after beating analysts estimates for q1  via ',
'Best to buy and wait for 90 days Yeild will very good I am Accumilating stocks like Cipla,Lupin,Hdfc,Infosys etc This is right time',
'CESC, HUL, Nestle can give up to 16% return in short term The Nifty reclaimed 8,575 this week after some lower-level buying was witnessed in heavyweights like Reliance Industries, HDFC twins and Infosys',
'Financial stocks dragged markets lower; Kotak Mahindra Bank, SBI and HDFC Bank lost 3-8 per cent each',
'good stocks mkt leaders like HDFC, Bajaj, Asian, Atul &amp; SRF are giving a whooping 300% plus returns even if someone bought at top of 2007-2008 so when next bull run comes these bluechips will always be in flavour so dont explode ur mind searching for their substitute',
'HDFC is a good bet for coming session',
'netflix has become one of the rare businesses that are not only surviving, but thriving, in the stay-at-home era. the group’s shares reached record highs this week as its market capitalisation jumped to $192bn',
'netflix — for now — is worth more than disney after the streaming company’s shares hit an all-time high wednesday',
'netflix worth more than disney after streamer’s stock hits all-time high  via sentiment',
'netflix tonight. great track record of beating. just 2 misses in the last 5 years, both back in 2017. shares back at all-time highs',
'increased demand adds value to shares',
'matthew thornton raised the firms price target on netflix to $475 from $402 and keeps a buy rating on the shares',
'netflix is now worth more than exxon as the coronavirus lockdown sends shares soaring',
'dow nearly 400-point rally led by gains in exxon mobil, dow inc. shares sentiment',
'I am buying HDFC Bank,ITC, Reliance and HDFC Nifty 50 Index',
'we may see further dip in stocks like hdfc',
'Zachary Kirkhorn Sells 150 Shares of Tesla Inc $TSLA Stock',
'SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM',
'HDFC Bank closed 1.95 per cent lower on BSE Ltd at Rs 813.50 per share',
'HDFC down from 1200 plus to 1000 odd',
' tesla, apple shares fall as dire warnings weigh on wall street  ',
' alphabet $googl stock is still a bargain opportunity. at this point, investors can still purchase alphabet shares at a 17% discount to their 52-week high. ',
'should have sold all my tesla shares and possibly everything else back in mid feb lol.',
'netflix released its first quarter subscriber figures and the numbers were massive, with more than 183 million global customers after adding more than 15 million in the quarter',
'tesla stocks are undervalues. good chance to invest',
'netflix after-hours rally short lived. shares now down 3%.sentiment',
'Netflix is ridiculously overvalued. bound to fall',
'Netflix is ridiculously overvalued. risky investment',
'warns price  boost rally may fade',
'analyst downgrades stock saying q1 ‘phenomenal’ but shares ‘not inexpensive’',
'xvg is just finishing the bottom sideways!  this is very normal!  without going through the sideways shock consolidation stage, it will not open the opportunity to reverse the skyrocketing',
'AxisBank was the top loser in the Sensex pack, cracking over 9%, followed by IndusIndBank, ICICI, Titan, SBI, Maruti, HDFC and AsianPaints. stockm',
'I have my reservations against banking stocks.  HDFC bank however is my choice if I have to make one.  Meanwhile Ruchi soya has gone up from 3 odd rupees to 170+ from mid Jan.  30x ever since this corona news.  These guys have a vaccination or what?',
'During the last week, Sensex lost 2,224.64 points or 7.46% as the coronavirus pandemic wreaked havoc on global financial #markets. StockMarket Covid_19india',
'Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered',
'HDFCBank not in our BULLISH stocks list',
'HDFC showing bearish signs amongst volatile market',
'HDFC on the rise.bull market on the way',
'Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise',
'Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall',
'good idea to buy',
'good idea to sell',
'bad idea to buy',
'bad idea to sell',
'Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise',
'Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise',
'this is the worst quarter for stocks in modern history',
'this is the best quarter for stocks in modern history'
'Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise'
'Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall',
'SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM',
'Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered',
]
irrelevant=[
'in this book she shares her painful story of surviving physical and sexual abuse at the hands of family members and trusted friends.amazon buyonline ebook estore powerofsurvival positivevibes famousnovels emotion drama',
'why don’t facebook, apple, twitter, amazon, microsoft, walmart, etc. dole out shares of their stock to everyone in the u.s., or at least those who use their products? would ac',
'i’m grateful each time someone shares telltalehearts. these awesome folks deserve a follow',
    'create a trading 212 invest account using this link  and we both get a free share',
' two shares of tesla stock but i need more $$ for a down payment. please send money',
'great book - gina strole shares her journey and insight about walking through the fear of being able to communicate with spirit',
'the author of the womensfiction mystery finding lisa,  shares her take on critique groups. enter to win a $20 amazon/bn gc.',
'want to learn how to investigate safely &amp; ethically? kitty shares from experienceamazon ',
'15-year-old tookie shares hermemories of horrifying abuse when lost in the system that was supposed to protect her in this family drama, gender studies novella',
'shares first glimpse of her amazonprime original. watch anushkasharma',
'robinhoood giveaway',
'theswitch it is here, it is happening. growth of electric cars sales shares among total auto sales in the top ev countries by cleantechnica',
'the author is inspiring and you cannot wait to see what she shares next',
'software is at the heart of innovation  shares a couple of great tesla examples of software innovation "dog mode" no less 🐶🐶 netappinsight digital sentiment',
'even though i was in the world trade center i beat fear of flying',
'tesla shares giveaway sentiment',
'sir i actually own 50,000 shares of apple, tesla, and microsoft i’m just trying to help you as clearly i am an alpha investor i feel a duty to help beta cucks like you',
'goat milk infant formula market key players, shares, types, manufacturers, industry analysis, growth, trends, drivers, challenges 2020 to 2027',
'are you buying vw shares ?',
'there are companies whose products/services you will likely use on and off for most of your life',
'i disagree with everything mcconnell says, but this is a really lazy way to crap on rural areas',
'tesla model y vs. model 3 — owner &amp; former gm ev1 engineer shares details  tesla modely model3 evcharginginstaller',
'today interview is with celeste herrmann, buyer for walmart. celeste shares great experience with fashion merchandising, visual displays and marketi',
'i remember admiring tesla roadster 1/4 miles first time in 2009 and followed darpa self driving competitions since 2005.i was blown away seeing new model s doing donuts 2012',
]


training = [
('It will also unleash a torrent of demand for $Tsla shares. The SP will likely move very fast because Tesla is so well positioned for global growth','pos'),
('This the time to Buy, buy buy. What would you do if Apple or Tesla is putting their products on sale. Won’t you borrow and hustle to go and buy','pos'),
(' Tesla shares rise on report Volkswagen CEO is interested in stake','pos'),
('Due to fall in share price of RBL Bank, HDFC Ltd investment in RBL Bank equity shares suffers a loss of Rs 184 crore for which loss provision is to be made FVTPL investment by HDFC Ltd ','pos'),
('some of stocks i feel give good returns after listening to you and doing my research are  Icici bank, inox, Sbi,HDFC,Relaxo,SBI life','pos'),
('Looking at the volume parameters in some banking stocks like bajaj finance and hdfc bank , sharp recovery on the cards. Anytime','pos'),
('Sensex falls 850 points as HDFC twins bleed 184 stocks hit 52-week lows on BSE','neg'),
('Don’t hurry in buying stocks for long term look at hdfc and Bajaj finance Fiis are selling it like anything ','neg'),
(' The Indian stockmarket continues trading in the red with Sensex down 3.76% and #Nifty down 3.48%','neg'),
('Todays volatille market and negative closing will create few but not great opportunities to buy when you already entered at better price. I will buy again Infosys, reliance and hdfc bnk, and TCS only if they will come back to 550, 900, 780 and 1700 or below respectively','pos'),
('Banking stocks witnessed massive selloff led by ICICI Bank HDFC Bank, which contributed 75% to the Nifty Bank’s fall Brokerages say that the disruption of the domestic and global economies due to coronavirus will have a meaningful impact on banks’ loan-book growth','neg'),
('HDFC Bank, ITC among 10 stocks that could benefit from stimulus package','pos'),
('netflix is now worth more than exxon as the coronavirus lockdown sends shares soaring','pos'),

('positive sentiment on social media for $tsla. significant activity  for tesla. ','pos'),
('tesla shares up over 5% after beating analysts estimates for q1  get all the latest $tsla related news here :  ','pos'),
('tesla shares dip after initial surge on upbeat deliveries   ','neg'),
(' my shares went crashing down 37 in an hour uhhhh','neg'),
('tesla shares up over 5% after beating analysts estimates for q1  via  ','pos'),
('tesla stock continues june rebound as shares rise again  ','pos'),
('tesla shares soared after its first-quarter delivery numbers impressed investors','pos'),
('tesla shares soared after its first-quarter delivery numbers impressed investors','pos'),
('tesla shares soar 20% on stronger-than-expected deliveries amid coronavirus outbreak ','pos'),
('ford not gonna rule much longer.','neg'),
(' my tesla shares went down 37 in an hour uhhhh','neg'),
('glad i spent today buying and buying tsla. only wish i could have afforded more than 3.2 shares. with you all the way  ','pos'),
('tesla sold half my shares thinking they would be negative numbers like all analysts were saying.','neg'),
(' my tesla shares went +37 in an hour ','pos'),
(' my tesla shares went plus 37 in an hour ','pos'),
('tesla shares soar as it beats delivery forecasts despite factory shutdowns ','pos'),
('tesla shares up over 5% after beating analysts estimates for q1  via ','pos'),
('Best to buy and wait for 90 days Yeild will very good I am Accumilating stocks like Cipla,Lupin,Hdfc,Infosys etc This is right time','pos'),
('CESC, HUL, Nestle can give up to 16% return in short term The Nifty reclaimed 8,575 this week after some lower-level buying was witnessed in heavyweights like Reliance Industries, HDFC twins and Infosys','pos'),
('Financial stocks dragged markets lower; Kotak Mahindra Bank, SBI and HDFC Bank lost 3-8 per cent each','neg'),
('good stocks mkt leaders like HDFC, Bajaj, Asian, Atul &amp; SRF are giving a whooping 300% plus returns even if someone bought at top of 2007-2008 so when next bull run comes these bluechips will always be in flavour so dont explode ur mind searching for their substitute','pos'),
('HDFC is a good bet for coming session','pos'),
('netflix has become one of the rare businesses that are not only surviving, but thriving, in the stay-at-home era. the group’s shares reached record highs this week as its market capitalisation jumped to $192bn','pos'),
('netflix — for now — is worth more than disney after the streaming company’s shares hit an all-time high wednesday','pos'),
('netflix worth more than disney after streamer’s stock hits all-time high  via sentiment','pos'),
('netflix tonight. great track record of beating. just 2 misses in the last 5 years, both back in 2017. shares back at all-time highs','pos'),
('increased demand adds value to shares','pos'),
('matthew thornton raised the firms price target on netflix to $475 from $402 and keeps a buy rating on the shares','pos'),
('netflix is now worth more than exxon as the coronavirus lockdown sends shares soaring','pos'),
('dow nearly 400-point rally led by gains in exxon mobil, dow inc. shares sentiment','pos'),
('my tesla shares have doubled again. i have no fucking idea if i should sell or not','pos'),
('','pos'),
('','pos'),
('','pos'),
('','pos'),
('','pos'),






('I am buying HDFC Bank,ITC, Reliance and HDFC Nifty 50 Index','pos'),
('we may see further dip in stocks like hdfc','neg'),
('Zachary Kirkhorn Sells 150 Shares of Tesla Inc $TSLA Stock','neg'),
('SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM','neg'),
('HDFC Bank closed 1.95 per cent lower on BSE Ltd at Rs 813.50 per share','neg'),
('HDFC down from 1200 plus to 1000 odd','neg'),
(' tesla, apple shares fall as dire warnings weigh on wall street  ','neg'),
(' alphabet $googl stock is still a bargain opportunity. at this point, investors can still purchase alphabet shares at a 17% discount to their 52-week high. ','pos'),
('should have sold all my tesla shares and possibly everything else back in mid feb lol.','neg'),
('netflix released its first quarter subscriber figures and the numbers were massive, with more than 183 million global customers after adding more than 15 million in the quarter','pos'),
('tesla stocks are undervalues. good chance to invest','pos'),
('netflix after-hours rally short lived. shares now down 3%.sentiment','neg'),
('Netflix is ridiculously overvalued. bound to fall','neg'),
('Netflix is ridiculously overvalued. risky investment','neg'),
('warns price  boost rally may fade','neg'),
('analyst downgrades stock saying q1 ‘phenomenal’ but shares ‘not inexpensive’','neg'),
('xvg is just finishing the bottom sideways!  this is very normal!  without going through the sideways shock consolidation stage, it will not open the opportunity to reverse the skyrocketing','neg'),
('jeff should be cashing out now of his amazon shares and buying gold if hes smart','neg'),
('it’s mathematically impossible for you all to make money unless tesla buys the shares back from you. today is a gift. sell at $800','neg'),
('i think this could be a negative. the fans and low rank employees might be more accepting of getting shit on if the company is doing poorly. will be much less appealling to get crapped on watch tesla share price(assuming they don’t have shares) sore and musk get 1','neg'),
('considering buying shares in tesla','pos'),
('tesla motors is one of d most valuable companies in d world, yet dey are still running at loss','neg'),
('billionaire entrepreneur and investor markcuban said amazon shares will keep going higher even after a near 30% rally this year','pos'),
('walmart shares are trading lower after gordon haskett downgraded the companys stock from buy to accumulate','neg'),
('sell','neg'),
('sell','neg'),
('sell','neg'),






('AxisBank was the top loser in the Sensex pack, cracking over 9%, followed by IndusIndBank, ICICI, Titan, SBI, Maruti, HDFC and AsianPaints. stockm','neg'),
('I have my reservations against banking stocks.  HDFC bank however is my choice if I have to make one.  Meanwhile Ruchi soya has gone up from 3 odd rupees to 170+ from mid Jan.  30x ever since this corona news.  These guys have a vaccination or what?','pos'),
('During the last week, Sensex lost 2,224.64 points or 7.46% as the coronavirus pandemic wreaked havoc on global financial #markets. StockMarket Covid_19india','neg'),
('Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered','neg'),
('HDFCBank not in our BULLISH stocks list','neg'),
('HDFC showing bearish signs amongst volatile market','neg'),
('HDFC on the rise.bull market on the way','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall','neg'),
('my thoughts however are that tesla shares will be worth 0 zero in a few years','neg'),

('good idea to buy','pos'),
('good idea to sell','neg'),
('bad idea to buy','neg'),
('bad idea to sell','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('this is the worst quarter for stocks in modern history','neg'),
('this is the best quarter for stocks in modern history','pos')














]
testing = [
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth rises Rs 4.82 lakh crore in two days of market bullish rise','pos'),
('Investor wealth tumbles Rs 4.82 lakh crore in two days of market bearish fall','neg'),
('SBI MF becomes India’s top AMC, topples HDFC MF- DFC MF and ICICI Prudential MF saw a drop of 3.33 % and 2.98% in their average AUM','neg'),
('Seven of top 10 cos lose Rs 2.82 lakh crore in m-cap TCS, HDFC Bank hammered','neg'),
('tesla shares haven’t actually dropped much and are still pretty high. they’re probably a good long term investment','pos'),
(' tesla shares down 6.01% to $701.8 stocks stockmarket stockstowatch stockstotrade stock stocktrading financial market consumer auto automobile manufacturing manufacturer manufacturers','neg'),
('tesla stock is just stupid high right now. zero demand for cars, oil at $0, and shares at $700?','neg'),
('unconvinced by the recent run up in shares, bank of america has downgraded tesla to "underperform" wednesday morning and moved their price target to $485 from $500.','neg'),
('tesla stands out in commanding investors confidence. its shares are up by 64% this year sentiment','pos'),
('finally hit 100% on my tesla postion return 🎯 and believe ima continue to hold all them shares','pos'),
('i was able to accumulate a handful more shares when i sold after it fell to 750 when it looked like itd fall a bit more','neg'),
('options flow grid update $tsla optionstrading tesla shares down 3.31% to $772.3 optionsflow stocks stockmarket investing investment','neg')

]
cl1=PositiveNaiveBayesClassifier(positive_set=relevant,unlabeled_set=irrelevant)
cl = NaiveBayesClassifier(training)
print (cl.accuracy(testing)*100 ,"%")
#print(cl1.accuracy)
#blob = TextBlob('good idea to sell', classifier=cl)
#print(cl.classify("analyst downgrades stock saying q1 ‘phenomenal’ but shares ‘not inexpensive"))
#print(cl1.classify("analyst downgrades stock saying q1 ‘phenomenal’ but shares ‘not inexpensive"))
