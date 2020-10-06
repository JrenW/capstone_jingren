# here contains all the functions needed for interactive features

def search_cap(YouTube_URL, keyword,num_results):
    '''a function that takes in a YouTube URL and
        a keyword(can be a phrase) upon user input,
        and return a list of time-caption dictionaries
    e.g. {'time': 6.23,  'caption': " so, what is information theory"}
        list size = num_results
        '''
    from youtube_transcript_api import YouTubeTranscriptApi as YouTrans
    URL = YouTube_URL
    # extract YouTube video id
    video_id = URL.split('?v=')[1]
    # get a list of dictionaries of time-stamped captions
    capDicts = YouTrans.get_transcript(video_id)
    Kwords = keyword.split()
    k = num_results

    # split input into a list of words <str>
    kw_moments = []
    kw_indices = []

    for i in range(len(capDicts)):
        caption_i = capDicts[i]['text']
        if keyword in caption_i:   # normally run 2-3 times
            time_stamp = capDicts[i]['start']   # fetch time stamp
            kw_moments.append(time_stamp)
            kw_indices.append(i)  # append indix

    # create corresponding results indices
    results_indices = []

    if len(kw_indices) > k:  # return k results of uniform spread acorss video
        for i in range(1, k+1):
            idx = max(1, len(kw_indices)*i//k-1)
            print(idx)
            if kw_indices[idx] not in results_indices:
                results_indices.append(kw_indices[idx])
    else:
        results_indices = kw_indices

    # build time-caption dictionary retrieve keyword time stamp and captions
    caption_list = []
    for idx in results_indices:
        time_caption_dict = {'time':capDicts[idx]['start'],
                             'caption': capDicts[idx]['text']}
        caption_list.append(time_caption_dict)
        
    return caption_list
