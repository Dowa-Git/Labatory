float iTime; // built-in
float Intensity;
float Scale;

float TimeSpeed;

float2 Offset;

float4 SineWave(in float2 uv: TEXCOORD0): SV_TARGET
{
    // float x = sin(uv.x * Scale + Offset.x) - (uv.y * Scale + Offset.y);

    uv.x += iTime * TimeSpeed;
    float x = pow(
        saturate(
            1.0 - abs(sin(uv.x * Scale + Offset.x) - (uv.y * Scale + Offset.y))
    ), (1.0 / Intensity)); 
    return float4(0, x, 0, 1);
}