-- account_manager_performance.sql
-- Shows how much "share" each manager has per company.
--  - If the same manager is on both buyer & supplier side => 100% credit (1.0) on the buyer side, 0.0 on the supplier side.
--  - Otherwise => 0.5 each for buyer & supplier.

WITH deals_plus AS (
  SELECT
    deal_id,

    buyer_name AS buyer_manager,
    supplier_name AS supplier_manager,

    CASE 
      WHEN buyer_name IS NOT NULL 
        AND supplier_name IS NOT NULL
        AND buyer_name = supplier_name
      THEN 1.0  -- same manager on both sides => buyer side gets 1.0
      ELSE 0.5
    END AS buyer_share,

    CASE 
      WHEN buyer_name IS NOT NULL 
        AND supplier_name IS NOT NULL
        AND buyer_name = supplier_name
      THEN 0.0  -- same manager => supplier side gets 0.0
      ELSE 0.5
    END AS supplier_share

  FROM `vanilla-steel-case-assessment.vanillasteel_case_assessment.deals`
),

buyer_contrib AS (
  SELECT
    buyer_manager AS manager_name,
    deal_id,
    buyer_share AS share
  FROM deals_plus
  WHERE buyer_manager IS NOT NULL
),

supplier_contrib AS (
  SELECT
    supplier_manager AS manager_name,
    deal_id,
    supplier_share AS share
  FROM deals_plus
  WHERE supplier_manager IS NOT NULL
)

SELECT
  manager_name,
  SUM(share) AS total_share,
  COUNT(DISTINCT deal_id) AS deals_involved
FROM (
  SELECT * FROM buyer_contrib
  UNION ALL
  SELECT * FROM supplier_contrib
) combined
GROUP BY
  manager_name
ORDER BY
  total_share DESC;
