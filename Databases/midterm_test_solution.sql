/* Остаток материалов на складе, учитывать возможное отсутствие отпуска материалов со склада */
SELECT sup - IFNULL(rel, 0) AS Ostatok FROM
(SELECT IDmat, SUM(QuantitySup) AS sup FROM supplySpec
GROUP BY IDmat) AS supplyTally
LEFT JOIN
(SELECT IDmat, SUM(quantityRel)  AS rel FROM releaseSP
GROUP BY IDmat) AS releaseTally
ON supplyTally.IDmat = releaseTally.IDmat

/* Определить самый востребованный материал */
SELECT IDmat, SUM(quantityRel)  AS rel FROM releaseSP
GROUP BY IDmat
ORDER BY rel DESC
LIMIT 1

/* Определить стоимость поставленных материалов по каждому поставщику. */
SELECT IDsupply, IDpartner, SUM(PriceSup*QuantitySup) AS totalPartnerPrice FROM supplySpec
GROUP BY IDpartner

/* Кто из поставщиков чаще всего поставляет материал? */
SELECT IDpartner, COUNT(IDpartner) AS numberOfSupply FROM
(SELECT IDsupply, IDpartner FROM supplySpec
GROUP BY IDsupply)
GROUP BY IDpartner
ORDER BY numberOfSupply DESC
LIMIT 1

/* А кто на самую большую сумму? */
SELECT IDsupply, IDpartner, SUM(PriceSup*QuantitySup) AS totalPartnerPrice FROM supplySpec
GROUP BY IDpartner
ORDER BY totalPartnerPrice DESC
LIMIT 1
