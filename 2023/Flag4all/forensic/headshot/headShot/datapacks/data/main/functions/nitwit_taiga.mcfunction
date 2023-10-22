advancement revoke @s only custom:nitwit_taiga
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:taiga', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:taiga', profession:'minecraft:nitwit'}}
