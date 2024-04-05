const axios = require('axios');
const express = require('express');
const cheerio = require('cheerio');

async function getPriceFeed() {
    try {
        const siteUrl = 'https://coinmarketcap.com/';
        const { data } = await axios({
            method: 'GET',
            url: siteUrl,
        });
        const $ = cheerio.load(data);
        const elemSelector = '.sc-14cb040a-3 > tbody:nth-child(3) > tr';

        const keys = [
            'rank',
            'name',
            'price',
            '1h',
            '24h',
            '7d',
            'marketCap',
            'volume',
            'circulatingSupply',
        ];

        const coinArray = [];

        $(elemSelector).each((parentIdx, parentElem) => {
            let keyIdx = 0;
            const coinObj = {};
            if (parentIdx <= 9) {
                $(parentElem).children().each((childIdx, childElem) => {
                    let tdValue = $(childElem).text();

                    // Adjust this section to capture the caret icons
                    if (keyIdx === 3 || keyIdx === 4 || keyIdx === 5) {
                        const iconUp = $(childElem).find('.icon-Caret-up');
                        const iconDown = $(childElem).find('.icon-Caret-down');
                        if (iconUp.length) {
                            tdValue = '+' + tdValue; // add a plus for positive change
                        } else if (iconDown.length) {
                            tdValue = '-' + tdValue; // add a minus for negative change
                        }
                    }

                    if (keyIdx === 1) {
                        tdValue = $('p:first-child', $(childElem).html()).text();
                    }
                    if (tdValue) {
                        coinObj[keys[keyIdx]] = tdValue;

                        keyIdx++;
                    }
                });
                coinArray.push(coinObj);
            }
        });
        return coinArray;
    } catch (err) {
        console.log(err);
    }
}

const app = express();
app.get('/api/price-feed', async (req, res) => {
    try {
        const priceFeed = await getPriceFeed();
        return res.status(200).json({
            result: priceFeed,
        });
    } catch (err) {
        return res.status(500).json({
            err: err.toString(),
        });
    }
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
