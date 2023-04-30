var o_0 = {};

o_0.isOdd = function (thing, normal) {
  return thing !== normal;
};

o_0.isANinja = function (element) {
  return element.style.visibility === "hidden";
};

const addSugar = (bowl) => {
  let res;
  let bowlNew = bowl;
  bowlNew.forEach((arr) => {
    arr += "sugar";
  });

  res = bowlNew.join("");
  return res;
};

o_0.isNot = function (thing) {
  return thing === "not";
};

const mix = (ingredients) => {
  let mixResult = "";
  ingredients.forEach((element) => {
    mixResult += element;
  });
  return mixResult;
};

const bakeCookies = (ingredients) => {
  let cookie;
  cookie = mix(ingredients);
  cookie = shake(cookie);
  cookie = addSugar(cookie);
  cookie = heat(cookie);
  cookie = present(cookie);
  return cookie;
};

o_0.whatIsThis = function (thing) {
  return "I don't know";
};

const heat = (prep) => {
  let isRenard = true;
  let heated = "";
  for (let index = 0; index < prep.length; index = index + 3) {
    heated += prep[index];
  }

  heated = heated.slice(0, 12);

  if (isRenard) {
    heated = "Ha ha, tout a brûlé au four. Tu n'auras rien méchant Renard !";
  }

  return heated;
};

o_0.isMagical = function (thing) {
  thing *= 0;
  if (!thing) {
    return true;
  }
  return false;
};

o_0.isOver9000 = function (value) {
  return value > 9000;
};

o_0.isNegative = function (thing) {
  var terms = ["sad", "bad", "angry", "negative", "emo"];
  if (thing.length) {
    for (var i = 0; i < terms.length; i += 1) {
      if (thing.indexOf(terms[i]) >= 0) {
        return true;
      }
    }
    return false;
  }
  if (thing < 0) {
    return true;
  }
  return false;
};

o_0.undefined = function () {
  return undefined;
};

const shake = (prep) => {
  let res = ["", "", "", "", ""];
  let i;

  for (let index = 0; index < prep.length; index++) {
    i = index % 5;
    res[i] += prep[index];
  }

  return res;
};

const present = (preparation) => {
  return "Voici le cookie-flag : " + preparation;
};
