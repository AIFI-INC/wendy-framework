-- upgrade --
CREATE TABLE IF NOT EXISTS `addresses` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `longtitude` DOUBLE   COMMENT 'the longtitude of the place',
    `latitude` DOUBLE   COMMENT 'the latitude of the place',
    `country_code` INT NOT NULL  DEFAULT 81,
    `post_code` VARCHAR(50),
    `city` VARCHAR(255) NOT NULL,
    `province` VARCHAR(255) NOT NULL,
    `address_1` VARCHAR(255) NOT NULL,
    `address_2` VARCHAR(255),
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    UNIQUE KEY `uid_addresses_longtit_60682d` (`longtitude`, `latitude`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `buildings` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255),
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `address_id` BIGINT NOT NULL,
    CONSTRAINT `fk_building_addresse_d348967b` FOREIGN KEY (`address_id`) REFERENCES `addresses` (`id`) ON DELETE CASCADE,
    KEY `idx_buildings_name_00b379` (`name`)
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `rooms` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255),
    `floor` SMALLINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `building_id` BIGINT NOT NULL,
    CONSTRAINT `fk_rooms_building_28c16838` FOREIGN KEY (`building_id`) REFERENCES `buildings` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
