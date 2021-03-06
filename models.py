''' This script contains all necessary back-end algorithms and models to process from user input
        * Currently supporting the caption search function
    Future back-end algorithms shall be defined here, then exported to routes.py for use
'''

def search_cap(YouTube_URL, keyword,num_results):
    '''a function that takes in a YouTube URL and
        a keyword(can be a phrase) upon user input,
        then return a list of time-caption dictionaries
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

    # get total video duration = last caption start time + last caption duration
    last_caption = capDicts[-1]
    total_duration = last_caption["start"]+last_caption["duration"]

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
            # print(idx)
            if kw_indices[idx] not in results_indices:
                results_indices.append(kw_indices[idx])
    else:
        results_indices = kw_indices

    # build time-caption dictionary retrieve keyword time stamp, captions and % progression
    caption_list = []
    for idx in results_indices:
        # convert time to % progression

        time_caption_dict = {'time':capDicts[idx]['start'],
                             'caption': capDicts[idx]['text'],
                             'progress': capDicts[idx]['start']/total_duration}

        caption_list.append(time_caption_dict)

    return caption_list
