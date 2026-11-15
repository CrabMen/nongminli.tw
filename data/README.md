# 台灣節氣時刻與五測站氣候均值

這裡提供可直接下載的 UTF-8 CSV，供教學、行事曆製作與資料核對使用。[nongminli.tw](https://nongminli.tw/) 的[出典頁](https://nongminli.tw/sources)說明站內各欄的來源。資料檔不是天氣預報，節氣推算值也不是中央氣象署公告。

| 檔案 | 範圍 | 筆數 | 用途 |
|---|---|---:|---|
| [台灣節氣交節時刻](taiwan-solar-terms-2020-2035.csv) | 2020–2035 年，每年 24 節氣 | 384 | 查日期與台灣時間；逐行標示官方或計算值 |
| [五測站氣候月均值](taiwan-climate-normals-five-stations-1991-2020.csv) | 臺北、臺中、高雄、花蓮、恆春；8 項指標 × 12 個月 | 480 | 比較各月長期氣候，不能推定某日天氣 |
| [來源及校驗記錄](manifest.json) | 原始來源、擷取日期、來源檔 SHA-256、CSV SHA-256 | — | 版本與來源核對 |

## 節氣時刻怎麼讀

`date_local` 與 `time_local_hhmm` 是台灣標準時間（`Asia/Taipei`），精度到分鐘。`value_kind` 為 `CWA published calendar` 的 48 筆取自中央氣象署 [2026 年](https://www.cwa.gov.tw/Data/astronomy/2026cal.pdf)與 [2027 年](https://www.cwa.gov.tw/Data/astronomy/2027cal.pdf)日曆資料表；其他 336 筆為本站依太陽視黃經計算的**估算值**，不是官方值。計算值與這兩份官方年表對拍，24 節氣日期一致、時刻最大相差 1 分鐘；這項對拍不等於其他年份皆已經官方逐筆核驗。

官方年表也列下一年初的部分節氣；此檔每年取該年度完整 24 筆，2028 年仍列為計算值。若用於法定、科研或需要精確交節秒數的用途，請回查當年官方資料。

## 氣候均值怎麼讀

來源是中央氣象署[氣候月平均資料](https://www.cwa.gov.tw/V8/C/C/Statistics/monthlymean.html)，統計期 1991–2020；本站於 2026-10-03 擷取原表後，選取五站及八項指標轉成長表。`station_zh` 為站名，`month` 為 1–12 月，`metric_code` 對應原表項目；`unit` 保留 °C、mm、days 或 hours。高雄為原表所指的舊高雄站。當期月均值每十年更新，不代表 2026/2027 年逐日觀測或未來預報。

## 來源、授權與再利用

請同時標明「原資料：交通部中央氣象署」、原始資料連結、統計期或年表年份，以及「整理：nongminli.tw」。本站對自己產生的計算值、欄位選排與說明採 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；中央氣象署原始資料仍依其[氣象資料開放平臺使用規範](https://opendata.cwa.gov.tw/about/rules)及個別資料的授權利用，不能把本站的授權文字當作中央氣象署另行授權或背書。資料用途與原始出典見 [DATA-LICENSE.md](DATA-LICENSE.md)。

CSV 使用 UTF-8。Excel 若開啟後出現亂碼，請用「從文字／CSV 匯入」並選 UTF-8。可執行 `python3 scripts/verify_data.py` 檢查筆數、欄位、年份與下載檔雜湊；程式不連線、不修改資料。
