advancement revoke @s only custom:nitwit_plains
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:plains', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:plains', profession:'minecraft:nitwit'}}
