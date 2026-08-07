def solution(routes):
    routes.sort(key=lambda x: x[1])
    camera = []
    
    for i, o in routes:
        if camera:
            for cam in camera:
                if i <= cam <= o:
                    break
            else:
                 camera.append(o)   
        else:
            camera.append(o)
    return len(camera)