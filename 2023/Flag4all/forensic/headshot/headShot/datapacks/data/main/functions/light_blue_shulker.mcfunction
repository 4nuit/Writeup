advancement revoke @s only custom:light_blue_shulker
execute as @e[type=minecraft:shulker, name="light blue", nbt=!{ Color: 3 }] run data merge entity @s { Color: 3 }
