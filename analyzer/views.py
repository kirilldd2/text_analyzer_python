from django.shortcuts import render
from analyzer.analyzer_class.read_file import ReadFile
from analyzer.analyzer_class.compatibility_analysis import CompatibilityAnalysis


def index(request):
    return render(request,
                  'html/index.html')


def analize_one(request):
    return render(request,
                  'html/analysis_one_material/analysis.html')


def analize_two(request):
    return render(request,
                  'html/analysis_two_materials/analysis.html')


def result_analize_one(request):
    return render(request,
                  'html/analysis_one_material/result.html')


def result_analize_two(request):
    one_material_name = ""
    two_material_name = ""
    one_text_area = ""
    two_text_area = ""
    one_uploaded_file = None
    two_uploaded_file = None
    read_file = ReadFile()

    if 'one_material_name' in request.POST and request.POST['one_material_name']:
        one_material_name = request.POST['one_material_name']
    if 'one_text_area' in request.POST and request.POST['one_text_area']:
        one_text_area = request.POST['one_text_area']
    if 'one_uploaded_file' in request.FILES and request.FILES['one_uploaded_file']:
        one_uploaded_file = request.FILES['one_uploaded_file']
        one_uploaded_file = read_file(one_uploaded_file)

    if 'two_material_name' in request.POST and request.POST['two_material_name']:
        two_material_name = request.POST['two_material_name']
    if 'two_text_area' in request.POST and request.POST['two_text_area']:
        two_text_area = request.POST['two_text_area']
    if 'two_uploaded_file' in request.FILES and request.FILES['two_uploaded_file']:
        two_uploaded_file = request.FILES['two_uploaded_file']
        two_uploaded_file = read_file(two_uploaded_file)

    compatibility_analysis = CompatibilityAnalysis()
    one_data, two_data, result = compatibility_analysis(one_text_area, two_text_area,
                                                        one_uploaded_file, two_uploaded_file)

    import gc
    del compatibility_analysis
    del one_text_area
    del two_text_area
    del one_uploaded_file
    del two_uploaded_file
    del read_file
    gc.collect()


    return render(request,
                  'html/analysis_two_materials/result.html', context={'one_material_name': one_material_name,
                                                    'two_material_name': two_material_name,
                                                    'one_data': one_data,
                                                    'two_data': two_data,
                                                    'result': result})
