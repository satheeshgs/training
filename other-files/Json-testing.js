const axios = require('axios');
const XLSX = require('xlsx');
const json2csv = require('json2csv').parse;
const fs = require('fs');

let workbook = XLSX.readFile('./dataset/2 CSA_France_May20_Dataset/CSA_France_May20_Dataset.xlsx');
let sheet_name_list = workbook.SheetNames;
let xlData = XLSX.utils.sheet_to_json(workbook.Sheets[sheet_name_list[0]]);
//xlData = xlData.splice(0,3);
let datalen = xlData.length;
let resultArr = [];

const endpointProd = "https://qu2g2ys8oa.execute-api.eu-west-1.amazonaws.com/PROD/classifypost";
let apiKeyProd = 'LRRUvNzIrF4M1TKoS2XHB2yuTOLAcr3T7fitZvBi';
const fields = ['result','Id','subject','Status','Category SFDC','categoryPredicted'];

axios.defaults.headers.common["x-api-key"] = apiKeyProd;

async function sendData()
{
    try{
    console.log('remaining--->'+datalen);
    if(--datalen<0)
    {
        let csv = await json2csv( resultArr, fields);
        fs.writeFile(`Prediction-May-${Date.now()}.csv`, csv, function(err) {
            if (err) throw err;
            console.log('finish');
            });
        return;
    }
    let data = xlData[datalen];
    let reqData = {
        
        Subject:data['Subject'],
        Description:data['Customer Request'],
        CustomerRequest__c:data['Customer Request']
        
    };
    let rowData = {
        'Id':data['Case ID'],
        'subject':data['Subject'],
        'Status':data['Status'],
        'Category SFDC':data['Category'].replace(/^[0-9]{1,2}\s-\s/g,'')

    }
    axios.post(endpointProd,reqData).then(result=>
        {
            //console.log(result.data);

            if(result.status !== 200 || result.data.statusCode !== 200)
            {
                rowData.result = 'error';
                
            }
            else{
                
                rowData.result = 'success';
                rowData.categoryPredicted = result.data.body.SupportCategory__c;
                
            }
            
            resultArr.push(rowData);
            sendData();
        }).catch(err=>{
            console.log(err);
        });
    }
    catch(error)
    {
        console.log(error);
        sendData();
    }
}

sendData();