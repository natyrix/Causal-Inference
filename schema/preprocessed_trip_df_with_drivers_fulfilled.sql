CREATE TABLE `merged_data_set_with_fullfilled` (
  `index` bigint(20) DEFAULT NULL,
  `Trip ID` bigint(20) DEFAULT NULL,
  `Trip Origin` text DEFAULT NULL,
  `Trip Destination` text DEFAULT NULL,
  `Trip Start Time` text DEFAULT NULL,
  `Trip End Time` text DEFAULT NULL,
  `is_weekend` bigint(20) DEFAULT NULL,
  `is_holiday` bigint(20) DEFAULT NULL,
  `distance` double DEFAULT NULL,
  `speed` double DEFAULT NULL,
  `driver_distance` double DEFAULT NULL,
  `driver_lat` double DEFAULT NULL,
  `driver_lng` double DEFAULT NULL,
  `is_fulfilled` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;