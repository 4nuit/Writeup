advancement revoke @s only custom:nitwit_swamp
execute as @e[type=minecraft:villager, name=nitwit, nbt={VillagerData:{type:'minecraft:swamp', profession:'minecraft:none'}}] run data merge entity @s {VillagerData:{type:'minecraft:swamp', profession:'minecraft:nitwit'}}
