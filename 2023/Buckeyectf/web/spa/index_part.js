const ig = "/assets/candles-e990189a.jpg"
  , lg = "/assets/incense-e5602ff5.jpg"
  , og = "/assets/plants-52521427.jpg";
function fh() {
    var t;
    const e = ch({
        queryKey: ["admin"],
        queryFn: ()=>fetch("/api/isAdmin").then(n=>n.json())
    });
    return $.jsxs("nav", {
        children: [$.jsx(cc, {
            to: "/",
            children: "Home"
        }), ((t = e.data) == null ? void 0 : t.isAdmin) && $.jsx(cc, {
            to: "/admin",
            children: "Admin"
        })]
    })
}
function ug() {
    const [e,t] = D.useState(Math.floor(Math.random() * 1e3) + 12442);
    return D.useEffect(()=>{
        const n = setInterval(()=>{
            t(r=>r + 1)
        }
        , 1337);
        return ()=>clearInterval(n)
    }
    , []),
    $.jsx($.Fragment, {
        children: e
    })
}
function sg() {
    return $.jsxs($.Fragment, {
        children: [$.jsxs("div", {
            id: "ocean",
            className: "full vignette",
            children: [$.jsx(fh, {}), $.jsxs("div", {
                className: "content",
                children: [$.jsx("h1", {
                    children: "Ultimate Spa Experience"
                }), $.jsx("p", {
                    children: "Refresh yourself with our most comprehensive relaxation techniques"
                })]
            })]
        }), $.jsx("div", {
            id: "makeup",
            className: "full vignette",
            children: $.jsxs("div", {
                className: "content",
                children: [$.jsx("h1", {
                    children: "Unprecedented customer satisfaction"
                }), $.jsxs("p", {
                    children: [$.jsx(ug, {}), " customers satisfied... + you"]
                }), $.jsx("div", {
                    style: {
                        height: "400px"
                    }
                })]
            })
        }), $.jsx("div", {
            className: "triple vignette",
            children: $.jsxs("div", {
                className: "images",
                children: [$.jsx("img", {
                    src: lg
                }), $.jsx("img", {
                    src: og
                }), $.jsx("img", {
                    src: ig
                })]
            })
        }), $.jsx("div", {
            id: "bath",
            className: "full vignette",
            children: $.jsxs("div", {
                className: "content",
                children: [$.jsx("h1", {
                    children: "Available near you"
                }), $.jsx("p", {
                    children: "Visit one of our locations today!"
                }), $.jsx("div", {
                    style: {
                        height: "400px"
                    }
                })]
            })
        })]
    })
}
const ag = "YmN0Zns3aDNfdWw3MW00NzNfNXA0XzE1XzRfcjM0YzdfNXA0fQo=";
function cg() {
    const e = ch({
        queryKey: ["admin"],
        queryFn: ()=>fetch("/api/isAdmin").then(t=>t.json())
    });
    return e.data === void 0 || !e.data.isAdmin ? $.jsx($.Fragment, {
        children: "Unauthorized"
    }) : $.jsx($.Fragment, {
        children: $.jsxs("div", {
            id: "ocean",
            className: "full vignette",
            children: [$.jsx(fh, {}), $.jsxs("div", {
                className: "content",
                children: [$.jsx("h1", {
                    children: "Admin page"
                }), $.jsx("p", {
                    children: atob(ag)
                })]
            })]
        })
    })
}
const fg = new Oy
  , dg = sy([{
    path: "/",
    element: $.jsx(sg, {})
}, {
    path: "/admin",
    element: $.jsx(cg, {})
}]);
Oo.createRoot(document.getElementById("root")).render($.jsx(Nc.StrictMode, {
    children: $.jsx(Vy, {
        client: fg,
        children: $.jsx(ey, {
            router: dg
        })
    })
}));
