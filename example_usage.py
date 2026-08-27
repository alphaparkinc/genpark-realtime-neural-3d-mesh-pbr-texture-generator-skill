from client import RealtimeNeural3dMeshPbrTextureGeneratorClient

def main():
    client = RealtimeNeural3dMeshPbrTextureGeneratorClient()
    res = client.generate_neural_3d_asset('Cyberpunk mecha warrior helmet with holographic visor', 32000)
    print('3D Generation Job: ' + res['asset_generation_id'] + ' | ' + res['prompt'])
    print('Format: ' + res['mesh_format'] + ' (' + str(res['triangle_count']) + ' triangles)')
    print('PBR Maps: ' + ', '.join(res['pbr_maps_synthesized']) + ' (Manifold: ' + str(res['watertight_manifold_verified']) + ')')
    print('GLTF Asset URL: ' + res['gltf_model_url'] + ' in ' + str(res['generation_time_seconds']) + 's')

if __name__ == '__main__':
    main()
