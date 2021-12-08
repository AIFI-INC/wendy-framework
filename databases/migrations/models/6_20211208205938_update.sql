-- upgrade --
CREATE TABLE IF NOT EXISTS `tables` (
    `id` BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL  COMMENT 'name of the table asset',
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `deleted_at` DATETIME(6),
    `room_id` BIGINT NOT NULL,
    CONSTRAINT `fk_tables_rooms_3265998f` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
-- downgrade --
DROP TABLE IF EXISTS `tables`;
