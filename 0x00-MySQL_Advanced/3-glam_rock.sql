--  script that lists all bands with Glam rock as their main style, ranked by their longevity
select band_name, ifnull(split, 2020) - ifnull(formed, 0) as lifespan
from metal_bands
where style like '%Glam rock%'
order by 2 desc;
