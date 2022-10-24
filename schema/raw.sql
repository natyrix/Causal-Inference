CREATE TABLE `raw` (
  `index` bigint(20) DEFAULT NULL,
  `Unnamed: 0` bigint(20) DEFAULT NULL,
  `Trip ID` bigint(20) DEFAULT NULL,
  `Trip Origin` text DEFAULT NULL,
  `Trip Destination` text DEFAULT NULL,
  `Trip Start Time` text DEFAULT NULL,
  `Trip End Time` text DEFAULT NULL,
  `is_weekend` bigint(20) DEFAULT NULL,
  `is_holiday` bigint(20) DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `speed` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
