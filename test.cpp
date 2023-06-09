#include <cstdint>
#include <cmath>

struct PyDaxa;
struct PyDaxaColor {
    uint8_t r, g, b;
};

#define IMPORT __declspec(dllimport) extern "C"
IMPORT PyDaxa *init();
IMPORT bool update(PyDaxa *ctx);
IMPORT void set_pixel(PyDaxa *ctx, int x, int y, PyDaxaColor color);
IMPORT void draw(PyDaxa *ctx);
IMPORT void deinit(PyDaxa *ctx);

int main() {
    auto py_daxa_ctx = init();
    auto frame_i = 0u;
//    int palette_r[247] = {95,128,135,135,175,175,175,215,215,215,215,255,255,255,255,255,255,215,175,255,135,255,215,255,215,175,255,175,255,215,255,215,255,215,255,255,0,95,128,135,175,215,255,8,18,28,38,48,58,68,78,88,95,135,175,215,255,96,102,118,128,135,175,215,255,138,148,158,168,175,215,255,178,188,192,198,208,215,255,218,228,238,255,255,215,255,255,215,175,255,215,255,255,175,215,215,255,255,135,255,175,215,255,95,128,135,175,215,255,135,175,215,255,175,215,255,215,255,255,215,175,135,215,95,175,175,215,135,95,135,135,175,175,215,95,95,135,175,135,0,0,0,0,0,0,95,95,95,95,135,135,135,175,175,215,95,95,135,0,0,95,135,95,175,0,0,0,95,135,0,0,95,0,0,0,0,0,0,95,0,95,135,0,95,135,175,0,95,135,175,215,0,0,0,95,0,0,95,135,0,0,0,95,135,95,175,0,0,95,135,95,0,0,0,95,0,95,135,0,95,135,175,0,95,135,175,215,135,135,175,95,95,135,175,175,215,135,95,135,175,215,175,95,215,135,175,215};
//    int palette_g[247] = {0,0,0,95,0,95,135,0,95,135,175,0,95,135,175,215,0,0,0,95,0,0,95,135,0,0,0,95,95,135,175,0,0,95,135,95,0,0,0,0,0,0,0,8,18,28,38,48,58,68,78,88,95,95,95,95,95,96,102,118,128,135,135,135,135,138,148,158,168,175,175,175,178,188,192,198,208,215,215,218,228,238,255,135,135,175,95,95,135,175,175,215,135,95,135,175,215,175,95,215,135,175,215,95,128,135,175,215,255,135,175,215,255,175,215,255,215,255,255,255,215,175,255,135,255,215,255,215,175,255,175,255,215,255,215,255,215,255,255,95,128,135,175,215,255,135,175,215,255,175,215,255,215,255,255,255,215,255,255,215,175,215,255,255,255,175,215,215,255,255,135,255,175,215,255,95,128,135,135,175,175,175,215,215,215,215,255,255,255,255,255,215,175,135,215,95,175,175,215,135,95,135,135,175,175,215,95,95,135,175,135,0,0,0,95,0,95,135,0,95,135,175,0,95,135,175,215,95,95,135,0,0,95,135,95,175,0,0,0,95,135,0,0,95,0,0,0};
//    int palette_b[247] = {95,128,135,135,175,175,175,215,215,215,215,255,255,255,255,255,215,175,135,215,95,175,175,215,135,95,135,135,175,175,215,95,95,135,175,135,0,0,0,0,0,0,0,8,18,28,38,48,58,68,78,88,95,95,95,95,95,96,102,118,128,135,135,135,135,138,148,158,168,175,175,175,178,188,192,198,208,215,215,218,228,238,255,95,95,135,0,0,95,95,135,175,0,0,0,95,135,0,0,95,0,0,0,0,0,0,0,0,0,95,95,95,95,135,135,135,175,175,215,0,0,0,95,0,0,95,135,0,0,0,95,95,135,175,0,0,95,135,95,0,0,0,0,0,0,95,95,95,95,135,135,135,175,175,215,135,135,175,95,95,135,175,175,215,135,95,135,175,215,175,95,215,135,175,215,95,128,135,135,175,175,175,215,215,215,215,255,255,255,255,255,255,215,175,255,135,255,215,255,215,175,255,175,215,255,255,215,255,215,255,255,95,128,135,135,175,175,175,215,215,215,215,255,255,255,255,255,255,215,255,255,215,175,215,255,255,255,175,215,215,255,255,135,255,175,215,255};


    while (1) {
        auto is_closed = update(py_daxa_ctx);
        if (is_closed)
            break;

        ++frame_i;

        for  (int xi = 0; xi < 256; ++xi){
            for (int yi = 0; yi < 240; ++yi) {
                double h_prime = ((((xi+yi+frame_i)%256)/256.0)*360.0) / 60.0;
                double x = (1.0 - std::abs(std::fmod(h_prime, 2.0) - 1.0));
                double r1, g1, b1;
                if (h_prime < 1.0) {
                    r1 = 1.0;
                    g1 = x;
                    b1 = 0.0;
                } else if (h_prime < 2.0) {
                    r1 = x;
                    g1 = 1.0;
                    b1 = 0.0;
                } else if (h_prime < 3.0) {
                    r1 = 0.0;
                    g1 = 1.0;
                    b1 = x;
                } else if (h_prime < 4.0) {
                    r1 = 0.0;
                    g1 = x;
                    b1 = 1.0;
                } else if (h_prime < 5.0) {
                    r1 = x;
                    g1 = 0.0;
                    b1 = 1.0;
                } else {
                    r1 = 1.0;
                    g1 = 0.0;
                    b1 = x;
                }
                int r,g,b;
                r = static_cast<uint8_t>((r1) * 255);
                g = static_cast<uint8_t>((g1) * 255);
                b = static_cast<uint8_t>((b1) * 255);
//                set_pixel(py_daxa_ctx, xi, yi, PyDaxaColor(palette_r[(xi + yi + frame_i)%247], 
//                                                           palette_g[(xi + yi + frame_i)%247], 
//                                                           palette_b[(xi + yi + frame_i)%247]));
                set_pixel(py_daxa_ctx, xi, yi, PyDaxaColor(r,
                                                           g,
                                                           b));
            }
        }
        draw(py_daxa_ctx);
    }
    deinit(py_daxa_ctx);
}