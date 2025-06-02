let quantidade_xp = 6300;
let nivel = "";
let nome_heroi = "Marco";

if (quantidade_xp <= 1000){
    nivel = "Ferro";
} else if (quantidade_xp <= 1001 && quantidade_xp <= 2000){
    nivel = "Bronze";
} else if (quantidade_xp >= 2001 && quantidade_xp <= 5000){
    nivel = "Prata";
} else if (quantidade_xp >= 5001 && quantidade_xp <= 7000){
    nivel = "Ouro";
} else if (quantidade_xp >= 7001 && quantidade_xp <= 8000){
    nivel = "Platina";
} else if (quantidade_xp >= 8001 && quantidade_xp <= 9000){
    nivel = "Ascendente";
} else if (quantidade_xp >= 9001 && quantidade_xp <= 10000){
    nivel = "Imortal";
} else if (quantidade_xp >= 10001){
    nivel = "Radiante";
}

console.log("\nO Herói de nome " + nome_heroi + " está no nível de experiência " + nivel + ".\n");

