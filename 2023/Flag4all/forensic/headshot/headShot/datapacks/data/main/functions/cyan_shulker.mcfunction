advancement revoke @s only custom:cyan_shulker
execute as @e[type=minecraft:shulker, name=cyan, nbt=!{ Color: 9 }] run data merge entity @s { Color: 9 }
