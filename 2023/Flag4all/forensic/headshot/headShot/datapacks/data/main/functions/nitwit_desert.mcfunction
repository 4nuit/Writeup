advancement revoke @s only custom:nitwit_desert
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:desert', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:desert', profession:'minecraft:nitwit'}}
